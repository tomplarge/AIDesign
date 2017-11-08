import os, sys
import flask

from flask import Flask, redirect, url_for, request
from flask import render_template

from build_teams import *

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('make_teams'))

@app.route('/make_teams', methods = ['POST', 'GET'])
def make_teams(context = None):
    # if we're running
    if request.method == 'POST':
        classname = str(request.form['classname'])
        num_teams = int(request.form['numteams'])
        people = [{'name': 'Tom', 'feat_1':.15842, 'feat_2':.11582}, {'name': 'Sangrin','feat_1':.28832, 'feat_2':.22845}, {'name': 'Suman', 'feat_1':.35483, 'feat_2':.33574},
                    {'name': 'Jennifer','feat_1':.42372, 'feat_2':.44683}, {'name': 'Matt','feat_1':.55693, 'feat_2':.55293}, {'name': 'Mike','feat_1':.65632, 'feat_2':.66492},
                    {'name': 'Stephanie','feat_1':.73154, 'feat_2':.77482}, {'name': 'Abdul','feat_1':.84038, 'feat_2':.88102}, {'name': 'Lindsay','feat_1':.91327, 'feat_2':.99230}]
        features = ['feat_1', 'feat_2']
        context = build_teams(num_teams, people, features)
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
