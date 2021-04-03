from flask import Flask, jsonify, request, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/batch_jobs/')
def bach_jobs():
    if request.args.get(filter[submitted_after]):

    return jsonify({"links": { "self": "http://localhost:5000/batch_jobs"}})

if __name__ == '__main__':
    app.run(debug=True)
