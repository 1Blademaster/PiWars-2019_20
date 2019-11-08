from flask import Flask, render_template, url_for, request, jsonify
from robot import Robot

app = Flask(__name__)
robot = Robot()
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
    movement['speed'] = request.json
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
            robot.stop()
        else:
            movement['direction'] = 'left'
            robot.turnLeft(9999999)
    elif request.json == 'right':
        if movement['direction'] == 'left':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'right'
            robot.turnRight(9999999)
    elif request.json == 'up':
        if movement['direction'] == 'down':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'up'
            robot.forward(9999999)
    elif request.json == 'down':
        if movement['direction'] == 'up':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'down'
            robot.backward(9999999)
    else:
        print('Unknown input')

    return movement['direction']

if __name__ == '__main__':
    app.run(debug=True)
