from app import app
from flask import render_template, request, url_for, redirect, flash, session

@app.route('/')
def index():
    return render_template('index.html')

