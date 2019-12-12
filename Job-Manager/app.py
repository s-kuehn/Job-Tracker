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