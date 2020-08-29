from flask import Flask

selfy = Flask(__name__)

@selfy.route("/")
def home():
    return "This is my own home page!"



if __name__ == "__main__":
    selfy.run(host="0.0.0.0", port=80)
