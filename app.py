#https://www.techcoil.com/blog/how-to-use-flask-apscheduler-in-your-python-3-flask-application-to-run-multiple-tasks-in-parallel-from-a-single-http-request/

from flask import Flask, render_template, url_for, request, jsonify
import subprocess
import os
import sys
import time
from motorFunctions.robot import Robot

app = Flask(__name__)
robot = Robot()
movement = {
    'direction': None,
    'speed': None,
}

@app.route('/fetchSliderData', methods=['POST'])
def fetchSliderData():
    print(request.json)
    movement['speed'] = request.json
    return jsonify({'response': 'done'})

@app.route('/')
def remote():
    return render_template('index.html')

@app.route('/fetchKeyPressData', methods=['POST'])
def fetchKeyPressData():
    print(request.json)
    if request.json == 'left':
        if movement['direction'] == 'right':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'left'
            robot.turnLeft()
    elif request.json == 'right':
        if movement['direction'] == 'left':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'right'
            robot.turnRight()
    elif request.json == 'up':
        if movement['direction'] == 'down':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'up'
            robot.forward()
    elif request.json == 'down':
        if movement['direction'] == 'up':
            movement['direction'] = 'stopped'
            robot.stop()
        else:
            movement['direction'] = 'down'
            robot.backward()
    else:
        print('Unknown input')
        movement['direction'] = 'unknown'

    return movement['direction']

@app.route('/command')
def enterCommand():
    return render_template('command.html')

@app.route('/executeCommand', methods=['POST'])
def executeCommand():
    cmd = request.json.split()
    if cmd[0] == 'cd':
        os.chdir(cmd[1])
        files = ''
        for file in os.listdir(os.getcwd()):
            files += file + ' \n'
        return jsonify({'response': files})
    p = subprocess.Popen(cmd, cwd=os.getcwd(), stdout=subprocess.PIPE, shell=True)
    pOut = p.communicate()[0].decode()
    #exec(open('prin.py').read())
    return jsonify({'response': pOut})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
