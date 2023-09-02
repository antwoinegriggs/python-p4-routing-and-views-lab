#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count_route(parameter):
    count = f''
    for i in range(int(parameter)):
        count += f'{i}\n'
    return count

@app.route('/math/<int:a>/<string:opp>/<int:b>')
def math(a, opp, b):
    print(f"here: {opp}")
    op = {'+': a+b,
          '-': a-b,
          '*': a*b,
          'div': a/b,
          '%': a%b} 
    return f'{op[opp]}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
