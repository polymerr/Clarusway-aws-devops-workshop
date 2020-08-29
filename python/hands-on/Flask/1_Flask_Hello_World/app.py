from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!!!"

@app.route("/second")
def sec():
    return "This is second page!"

@app.route("/second/third")
def thr():
    return "This is 2nd's 3rd page!"

@app.route("/third/first")
def tf():
    return "this is real third's 1st page!!!"

@app.route("//<string:id>")
def var_id(id):
    return f"This is the {id}nd page!"


if __name__ == "__main__":
    app.run(debug = True)