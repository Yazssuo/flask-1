from flask import Flask
from flask import request
from operations import add, sub, mult, div

app = Flask(__name__)

calc_dict = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/<type>')
def do_func1(type):
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(calc_dict[type](a, b))

@app.route('/math/<type>')
def do_func2(type):
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(calc_dict[type](a, b))

# @app.route('/add')
# def web_add():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(add(a, b))

# @app.route('/sub')
# def web_sub():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(sub(a, b))

# @app.route('/mult')
# def web_mult():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(mult(a, b))

# @app.route('/div')
# def web_div():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(div(a, b))

