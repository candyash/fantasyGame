#!/bin/sh
cd ~/fantasyGame
virtualenv flask
source flask/bin/activate
cd ~/fantasyGame
pip install -r requirements.txt
