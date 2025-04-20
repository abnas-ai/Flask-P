

from flask import render_template
from app import app
from app.models import User

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)


from flask import render_template, redirect, url_for, flash

from app.models import Task, db



