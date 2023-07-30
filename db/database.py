import psycopg2

class Database:        
    def __init__(self, database="mentors", user="postgres", password="postgres", host="db", port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        