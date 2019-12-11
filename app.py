from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():



	if request.form:
		# Assign variables to form values
		project_name = request.form['project_name']
		description = request.form['description']
		due_date = request.form['due_date']
		shoot_date = request.form['shoot_date']
		purpose = request.form['purpose']
		budget = request.form['budget']
		special_requests = request.form['special_requests']

		# Add row to table and create table if not already existing
		conn = sqlite3.connect('calculations.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS joblist (
					id INTEGER PRIMARY KEY,
					project_name TEXT,
					description TEXT,
					due_date INTEGER,
					shoot_date INTEGER,
					purpose TEXT,
					budget INTEGER,
					special_requests TEXT)""")
		c.execute("INSERT INTO joblist(project_name, description, due_date, shoot_date, purpose, budget, special_requests) VALUES("+"'"+project_name+"'"+", "+description+", "+due_date+", "+shoot_date+", "+special_requests+")")
		c.execute("SELECT * FROM joblist")
		items = c.fetchall()
		for item in items:
			print(item)
		conn.commit()
		conn.close()
	return render_template('index.html', items=items)

@app.route('/submited')
def submitted():
	pass