from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
	# if request.method == 'POST':
	# 	pass
	return render_template('index.html')

@app.route('/submited')
def submitted():
	pass