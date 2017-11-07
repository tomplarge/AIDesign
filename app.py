import os, sys
import flask

from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('make_teams'))

@app.route('/make_teams', methods = ['POST', 'GET'])
def make_teams(context = None):
    # if we're running
    if request.method == 'POST':
        classname = request.form['classname']
        numteams = request.form['numteams']
        context = [[{'name': 'Tom'}, {'name': 'Sangrin'}, {'name':'Suman'}],
                   [{'name': 'Jennifer'}, {'name': 'Abdul'}, {'name':'Matt'}],
                   [{'name': 'Stephanie'}, {'name': 'Lindsay'}, {'name':'Mike'}],
                   [{'name': 'Stephanie'}, {'name': 'Lindsay'}, {'name':'Mike'}]]
        return render_template('make_teams.html', context=context)
    elif request.method == 'GET':
        return render_template('make_teams.html')

@app.route('/about')
def about():
    print 'about'
    return render_template('make_teams.html')

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
    return redirect(url_for('make_teams'))

if __name__ == '__main__':
    app.run(debug=True)
