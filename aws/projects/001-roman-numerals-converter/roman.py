from flask import Flask, request, render_template
from convroman import convert

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    num = request.form.get("number")

    if request.method == "POST" and ((not num.isdigit()) or ((int(num) > 3999) or (int(num) < 1))):
        not_valid = "not_validdd"
        return render_template("index.html", developer_name = "Muhammet POLAT", not_valid = "not_validdd")
        
    elif request.method == "POST":


        return render_template('result.html',number_roman = convert(num), number_decimal= num, developer_name = "Muhammet POLAT")

    else:
        return render_template("index.html", developer_name = "Muhammet POLAT")




if __name__ == '__main__':
    app.run(debug = True)
    # app.run(host='0.0.0.0', port=80)
