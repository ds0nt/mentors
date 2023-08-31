import os
import importlib

from utils.db import Database
# run pg.dump.sql migration

MIGRATIONS_TABLE = 'migrations_ran'
MIGRATIONS_PATH = 'db/migrations'

CODE_MIGRATIONS_TABLE = 'code_migrations_ran'
CODE_MIGRATIONS_PATH = 'db/code_migrations'

def _print(msg):
    print("migrate: {}".format(msg))

# create the two migrations tables
def _createMigrationTables(db: Database):
    cursor = db.cursor()    
    for table in [MIGRATIONS_TABLE, CODE_MIGRATIONS_TABLE]:            
        cursor.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='{}')".format(table))
        if cursor.fetchone()[0]:
            _print("{} table exists, moving on".format(table))
        else:
            cursor.execute("""
                CREATE TABLE {} (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """.format(table))
            db.commit()

def _insertMigration(db: Database, name, tableName):
    _print(f"inserting migration {name}, {tableName}")
    cursor = db.cursor()    
    cursor.execute(f"""
        INSERT INTO public.{tableName} (name)
        VALUES (%s)
        RETURNING id;
    """, (name,))
    return cursor.fetchone()[0]


def _getMigrationsRan(db: Database, tableName):
    cursor = db.cursor()    
    cursor.execute(f"SELECT name FROM public.{tableName}")
    migrations_ran = cursor.fetchall()
    migrations_ran = [m[0] for m in migrations_ran]
    return migrations_ran

def _sqlMigrate(db):
    _print("Running SQL migrations")

    migrations_ran = _getMigrationsRan(db, MIGRATIONS_TABLE)
    migrations = os.listdir(MIGRATIONS_PATH)
    migrations = [m for m in migrations if m not in migrations_ran]
    migrations.sort()

    if len (migrations) == 0:
        _print("No migrations to run")
        return
    
    # check that migrations are alphabetically after migrations_ran
    if len(migrations_ran) > 0:
        if migrations[0] < migrations_ran[-1]:
            _print("Migrations must be run alphabetical order, but {} comes after {}".format(migrations[0], migrations_ran[-1]))
            exit(1)
    
    for migration in migrations:
        _print("Running migration {}".format(migration))
        cursor = db.cursor()
        try:
            cursor.execute(open("{}/{}".format(MIGRATIONS_PATH, migration), "r").read())
            _insertMigration(db, migration, MIGRATIONS_TABLE)
        except Exception as e:
            _print("Error running migration: {}".format(e))
            db.conn.rollback()
            exit(1)
        db.conn.commit()
        _print("Migration {} ran successfully".format(migration))


def _pythonMigrate(db):
    _print("Running Python migrations")

    migrations_ran = _getMigrationsRan(db, CODE_MIGRATIONS_TABLE)
    migrations = os.listdir(CODE_MIGRATIONS_PATH)
    migrations = [m for m in migrations if m not in migrations_ran and m.endswith('.py')]
    migrations.sort()

    if len (migrations) == 0:
        _print("No code migrations to run")
        return
    
    # check that migrations are alphabetically after migrations_ran
    if len(migrations_ran) > 0:
        if migrations[0] < migrations_ran[-1]:
            _print("Code migrations must be run alphabetical order, but {} comes after {}".format(migrations[0], migrations_ran[-1]))
            exit(1)
    
    for migration in migrations:
        if not migration.startswith('_'):
            _print("Code migrations must start with an underscore")
            exit(1)
        _print("Running code migration {}".format(migration))
        try:
            codeMigration = importlib.import_module("{}.{}".format(CODE_MIGRATIONS_PATH, migration).replace('/','.').rsplit('.', 1)[0])
            codeMigration.migrate(db)
            _insertMigration(db, migration, CODE_MIGRATIONS_TABLE)
        except Exception as e:
            _print("Error running code migration, manual data repair may be needed: {}".format(e))
            exit(1)
        db.conn.commit()
        _print("Code migration {} ran successfully".format(migration))

# run migrations
# 1. create migration table if it does not exist using the utils/db connection
# 2. check db/migrations folder for migrations files
# 3. compile list of migrations that have not been run in alphabetical order
# 4. run migrations
def migrate(db: Database):
    _createMigrationTables(db)
    _sqlMigrate(db)
    _pythonMigrate(db)