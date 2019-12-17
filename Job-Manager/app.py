from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Home route
@app.route('/', methods=['GET','POST'])
def home():

	# Print contents of sql table
	conn = sqlite3.connect(os.path.realpath('../jobs.db'))
	c = conn.cursor()
	c.execute("SELECT * FROM joblist")
	jobs = c.fetchall()
	for job in jobs:
		print(job)
	conn.commit()
	conn.close()

	# Display index.html and pass in variables
	return render_template('index.html', jobs=jobs)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
	return render_template('dashboard.html')

@app.route('/joblist', methods=['GET','POST'])
def jobList():
	
	# Print contents of sql table
	conn = sqlite3.connect(os.path.realpath('../jobs.db'))
	c = conn.cursor()
	c.execute("SELECT * FROM joblist")
	jobs = c.fetchall()
	for job in jobs:
		print(job)
	conn.commit()
	conn.close()

	return render_template('joblist.html', jobs=jobs)

@app.route('/clientlist', methods=['GET','POST'])
def clientList():
	return render_template('clientlist.html')

@app.route('/calendar', methods=['GET','POST'])
def calendar():
	return render_template('calendar.html')

@app.route('/map', methods=['GET','POST'])
def map():
	return render_template('map.html')

@app.route('/messages', methods=['GET','POST'])
def messages():
	return render_template('messages.html')