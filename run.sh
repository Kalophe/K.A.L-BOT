#!/bin/bash
# Activate virtual environment and run bot

# create venv if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# activate venv
source venv/bin/activate

# upgrade pip (optional)
pip install --upgrade pip

# install requirements if not already installed
pip install -r requirements.txt

# run bot
python3 bot.py
