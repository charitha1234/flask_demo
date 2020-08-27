from app import app

from flask import request

@app.route('/')
def index():
    return "hello I'm charitha, what's your name"