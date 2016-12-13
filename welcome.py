import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return app.send_static_file('form.html')

@app.route('/output', methods=['POST'])
def my_form_post():
	num = int(request.form['number'])
	ret_string = ''
	
	if num % 4 == 0:
		ret_string = ret_string + 'IBM'

	if num % 7 == 0:
		ret_string = ret_string + ' Bluemix'
	
	return ret_string

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))