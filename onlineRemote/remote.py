from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

movement = {
    'direction': None,
    'speed': None,
}

@app.route('/slider')
def slider():
    return render_template('slider.html')

@app.route('/fetchSliderData', methods=['POST'])
def fetchSliderData():
    print(request.json)
    return jsonify({'response': 'done'})

@app.route('/keyPress')
def keyPress():
    return render_template('keyPress.html')

@app.route('/fetchKeyPressData', methods=['POST'])
def fetchKeyPressData():
    print(request.json)
    if request.json == 'left':
        if movement['direction'] == 'right':
            movement['direction'] = 'stopped'
        else:
            movement['direction'] = 'left
    elif request.json == 'right':
        if movement['direction'] == 'left':
            movement['direction'] = 'stopped'
        else:
            movement['direction'] = 'right
    elif request.json == 'up':
        if movement['direction'] == 'down':
            movement['direction'] = 'stopped'
        else:
            movement['direction'] = 'up
    elif request.json == 'down':
        if movement['direction'] == 'up':
            movement['direction'] = 'stopped'
        else:
            movement['direction'] = 'down
    else:
        print('Uknown input')
    
    return movement['direction']

if __name__ == '__main__':
    app.run(debug=True)
