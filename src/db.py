import psycopg2
import time

# Class Database is a class that provides db connections to the masses of classes
class Database:        
    def __init__(self, database="mentors", user="postgres", password="postgres", host="db", port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port        
        
        # retry connection
        retryLimit = 10
        retryCount = 0
        retryTimeout = 1
        while retryCount < retryLimit:
            try:
                self.conn = psycopg2.connect(
                    database=self.database,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                )
                print("Database connection successful")
                break
            except psycopg2.OperationalError as e:
                print("Database connection failed, retrying...")
                retryCount += 1
                time.sleep(retryTimeout)
                if retryCount == retryLimit:
                    raise e

    def cursor(self):
        return self.conn.cursor()
    
    def commit(self):
        self.conn.commit()