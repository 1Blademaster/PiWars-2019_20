from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/slider')
def slider():
    return render_template('slider.html')

@app.route('/fetchSliderData', methods=['POST'])
def fetchSliderData():
    print(request.json)
    return {'response': 'done'}

@app.route('/keyPress')
def keyPress():
    return render_template('keyPress.html')

if __name__ == '__main__':
    app.run(debug=True)
