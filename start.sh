#!/bin/bash
export FLASK_APP=run.py
export FLASK_DEBUG=1
echo "############### Running app ####################"
sleep 2
echo "############ Creating database #################"
sleep 2
flask run
