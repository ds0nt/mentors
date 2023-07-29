from flask import Flask
import psycopg2

app = Flask(__name__)

# connect to postgres
conn = psycopg2.connect("dbname=mentors user=postgres password=postgres host=db port=5432")

# return json list of mentors
@app.route("/mentors")
def mentors():
    return {
        "mentors": [
            {
                "id": 1,
                "name": "John Doe",
                "language": "English",
                "timezone": "PST",
                "description": "I'm a professional mentor with 10+ years of experience. I'm a good listener, and I'm very patient. I love helping people and I'm good at explaining things.",
                "reviews": [
                    {
                        "id": 1,
                        "reviewer": "Jane Doe",
                        "rating": 4,
                        "review": "John is a great mentor. He is very patient and explains things very clearly."
                    },
                    {
                        "id": 2,
                        "reviewer": "Jack Doe",
                        "rating": 3,
                        "review": "John is a great mentor. He is very patient and explains things very clearly."
                    }
                ]
            },
            {
                "id": 2,
                "name": "Jane Doe",
                "language": "English",
                "timezone": "EST",
                "description": "I'm a professional mentor with 10+ years of experience. I'm a good listener, and I'm very patient. I love helping people and I'm good at explaining things.",
                "reviews": [
                    {
                        "id": 1,
                        "reviewer": "John Doe",
                        "rating": 4,
                        "review": "Jane is a great mentor. She is very patient and explains things very clearly."
                    },
                    {
                        "id": 2,
                        "reviewer": "Jack Doe",
                        "rating": 3,
                        "review": "Jane is a great mentor. She is very patient and explains things very clearly."
                    }
                ]
            }
        ]            
    }