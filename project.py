from flask import Flask,render_template
from flask_misaka import Misaka
app=Flask(__name__)
Misaka(app)

@app.route('/')
def index():
	return render_template('index.html')


content1 = ""
with open('Introduction/Chapter-One.md', 'r') as f:
	content1 = f.read()
@app.route('/ichapterone')
def ichapterone():
	return render_template('page.html', text=content1)

content2 = ""
with open('Introduction/Chapter-Two.md', 'r') as f:
	content2 = f.read()
@app.route('/ichaptertwo')
def ichaptertwo():
	return render_template('page.html', text=content2)

content3 = ""
with open('Setup/Configuration/Chapter-One.md', 'r') as f:
	content3 = f.read()
@app.route('/sc')
def sc():
	return render_template('page.html', text=content3)

content4 = ""
with open('Setup/Installation/Chapter-One.md', 'r') as f:
	content4 = f.read()
@app.route('/si')
def si():
	return render_template('page.html', text=content4)

if __name__=="__main__":
	app.run(debug=True)