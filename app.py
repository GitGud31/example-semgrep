from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        eval(data)
        return 'ok'
    else:
        return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
