#!/bin/sh
#change to the project directory
cd  ~/fantasyGame
#The user own the project folder
sudo chown  $(whoami)  ~/fantasyGame

#Start the server
gunicorn --bind localhost:8000 manage:app
