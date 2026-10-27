@'
# Task 2: API Key Generation and Sharing

## Overview
This project implements a Flask REST API that processes text using API key authentication.

## Features
- Generates unique API keys for three consumers.
- Reads API keys securely from a local `.env` file.
- Accepts API keys through the `X-API-Key` request header.
- Validates API keys before processing requests.
- Converts submitted text to uppercase.
- Rejects missing or invalid API keys with HTTP 401.
- Rejects invalid JSON input with HTTP 400.

## Technologies
- Python
- Flask
- python-dotenv
- PowerShell for testing

## Project Files
- `app.py` - Flask API and authentication logic.
- `generate_keys.py` - Generates unique API keys.
- `requirements.txt` - Required Python packages.
- `.env` - Local API keys; do not upload this file publicly.
- `.gitignore` - Excludes secret and temporary files.

##Demo vedieo
Link: https://youtu.be/vouoV8Grqxw 
- `README.md` - Project documentation.

## Setup
From the main assignment directory, install dependencies:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r ".\Task_2_API_Key_Generation\requirements.txt"
