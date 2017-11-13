import os, sys
import flask
import json, csv

from flask import Flask, redirect, url_for, request
from flask import render_template

from build_teams import *

app = Flask(__name__)

@app.route('/')
def index(features = None, teams = None):
    # if we're running
    if request.method == 'POST':
        classname = str(request.form['classname'])
        num_teams = int(request.form['numteams'])

        people = json.load(open('static/people.json'))
        # features = json.load(open('static/traits.json'))

        input_feats = request.form.getlist('features')
        for i in range(len(input_feats)):
            input_feats[i] = str(input_feats[i])

        # # just testing
        # teams = []
        # teams.append(people[0:2])
        # teams.append(people[2:4])
        # teams.append(people[4:6])
        teams = build_teams(num_teams, people, input_feats)
        return render_template('index.html', teams = teams, features = input_feats)
    elif request.method == 'GET':
        print 'args: ', request.args
        classname = ""
        num_teams = 1
        people = json.load(open('static/people.json'))
        input_feats = []

        if 'classname' in request.args:
            classname = str(request.args['classname'])
        if 'numteams' in request.args:
            num_teams = int(request.args['numteams'])
        if 'features' in request.args:
            input_feats = request.args.getlist('features')
        for i in range(len(input_feats)):
            input_feats[i] = str(input_feats[i])
        teams = build_teams(num_teams, people, input_feats)

        return render_template('index.html', teams = teams, features = input_feats)

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
    return redirect(url_for('make_teams'))

if __name__ == '__main__':
    app.run(debug=True)
