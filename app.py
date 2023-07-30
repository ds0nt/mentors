from flask import Flask
app = Flask(__name__)

from db.database import Database
db = Database()

from db.mentor import create_table, insert, update, delete, get, get_all
create_table(db)

mentor1 = insert(
    db=db,
    first_name="mentor1",
    last_name="smith",
    email="smith1@gmail.com",
    phone="12341234",
    address="12341234 smith st.",
    specialization="Designer",
    experience_years="10",
    bio="I am a designer",
)

mentor2 = insert(
    db=db,
    first_name="mentor2",
    last_name="smith",
    email="smith2@gmail.com",
    phone="12341235",
    address="a smith st.",
    specialization="Receptionist",
    experience_years="104",
    bio="I am barely alive",
)


# return json list of mentors
@app.route("/mentors")
def mentors():
    mentors = get_all(db=db)
    return mentors