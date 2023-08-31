from flask import Flask
app = Flask(__name__)

from src.db import Database
db = Database()

from utils.migrations.migrate import migrate
migrate(db)

from models.mentor import get_all

# return json list of mentors
@app.route("/mentors")
def mentors():
    mentors = get_all(db=db)
    return mentors