from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('remote.html')

@app.route("/fetchData", methods=["POST"])
def fetchData():
    print(request.json)
    return {'response': 'done'}

if __name__ == '__main__':
    app.run(debug=True)
