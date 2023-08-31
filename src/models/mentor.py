from utils.db import Database

def insert(db: Database, first_name, last_name, email, phone, address, specialization, experience_years, bio):
    with db.cursor() as cursor:
        query = """
            INSERT INTO mentors (first_name, last_name, email, phone, address, specialization, experience_years, bio, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, now(), now())
            RETURNING id;
        """
        values = (first_name, last_name, email, phone, address, specialization, experience_years, bio)
        cursor.execute(query, values)
        return cursor.fetchone()[0]
    
def update(db: Database, id, first_name, last_name, email, phone, address, specialization, experience_years, bio):
    with db.cursor() as cursor:
        query = """
            UPDATE mentors
            SET first_name=%s, last_name=%s, email=%s, phone=%s, address=%s, specialization=%s, experience_years=%s, bio=%s, updated_at=now()
            WHERE id=%s
        """
        values = (first_name, last_name, email, phone, address, specialization, experience_years, bio, id)
        cursor.execute(query, values)
        return cursor.rowcount
    
