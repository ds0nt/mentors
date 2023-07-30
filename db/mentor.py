from db.database import Database

def create_table(db: Database):
    db.cur.execute("""
        CREATE TABLE IF NOT EXISTS mentors (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255),
            address VARCHAR(255),
            specialization VARCHAR(255),
            experience_years INTEGER,
            bio VARCHAR(255)
        );
    """)
    

def insert(db: Database, first_name, last_name, email, phone, address, specialization, experience_years, bio):
    query = """
        INSERT INTO mentors (first_name, last_name, email, phone, address, specialization, experience_years, bio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """
    values = (first_name, last_name, email, phone, address, specialization, experience_years, bio)
    db.cur.execute(query, values)
    print("inserting {} {}", query, values)
    return db.cur.fetchone()[0]

def update(db: Database, id, first_name, last_name, email, phone, address, specialization, experience_years, bio):
    query = """
        UPDATE mentors
        SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s, specialization = %s, experience_years = %s, bio = %s
        WHERE id = %s;
    """
    values = (first_name, last_name, email, phone, address, specialization, experience_years, bio, id)
    db.cur.execute(query, values)

def delete(db: Database, id):
    query = """
        DELETE FROM mentors WHERE id = %s;
    """
    values = (id,)
    db.cur.execute(query, values)

def get(db: Database, id):
    query = """
        SELECT * FROM mentors WHERE id = %s;
    """
    values = (id,)
    db.cur.execute(query, values)
    return db.cur.fetchone()

def get_all(db: Database):
    query = """
        SELECT * FROM mentors;
    """
    db.cur.execute(query)
    return db.cur.fetchall()
