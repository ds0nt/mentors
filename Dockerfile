FROM python:3.9-slim-buster

LABEL maintainer="flask-app"

# Setting the working directory
WORKDIR /app

# Copying requirements.txt to the container
COPY requirements.txt requirements.txt

# Installing the requirements
RUN pip3 install -r requirements.txt

# Copying the rest of the code into the container
COPY . .
VOLUME /app

# Setting the environment variable
ENV FLASK_APP=app.py

# Setting the port
EXPOSE 5000

# Run the flask app
CMD ["flask", "run", "--host=0.0.0.0"]
