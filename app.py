import os, sys
import flask

from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index(context = None):
    print 'index'
    return render_template('index.html')

@app.route('/about')
def about():
    print 'about'
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    print 'upload'
    print request.form
    files = request.files.getlist('file')
    for f in files:
        print f.read()
        # connect to api
        # do our clustering
        # return the teams
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
