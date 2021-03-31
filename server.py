from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/batch_jobs/')
def bach_jobs():
	return 'batch jobs!'

if __name__ == '__main__':
	app.run(debug=True)
