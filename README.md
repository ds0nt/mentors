
# Mentors

Backend for the Mentors app written using Python / Flask. Connects to a postgresql database. Has some migration logic and a mentors model for now.

# Running on local

In the project's root directory run these commands

```
# create virtual environment
python3 -m venv .venv
. .venv/bin/activate

# install dependencies with pip
pip install -r requirements.txt

# run dev server
flask --app app run
```

# Running in docker-compose

```
docker-compose build
docker-compose up
```
