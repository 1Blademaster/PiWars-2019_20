from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request)
    print(request.form)
    if request.method == 'POST':
        if 't1' in request.form:
            print('Bringing down Target 1')
        elif 't2' in request.form:
            print('Bringing down Target 2')
        elif 't3' in request.form:
            print('Bringing down Target 3')
        elif 't4' in request.form:
            print('Bringing down Target 4')
        return render_template('index.html', text='My Text')
    else:
        return render_template('index.html', text='My Text')

if __name__ == '__main__':
    app.run(debug=True)