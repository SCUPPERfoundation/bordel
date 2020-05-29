from flask import render_template

from . import app
from .models.alpha import ReviewDoc

@app.route('/')
def index():
    page = 1 # shim. fully deal with pagination later
    blobs = ReviewDoc.query.paginate(page)
    return render_template('home.html', blobs=blobs)

