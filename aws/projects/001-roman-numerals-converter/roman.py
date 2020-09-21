
from flask import Flask, request, render_template


app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def home():
    num = request.form.get("number")

    if request.method == "POST" and ((not num.isdigit()) or ((int(num) > 3999) or (int(num) < 1))):
        not_valid = "not_validdd"
        return render_template("index.html", developer_name = "E2248-Muhammet", not_valid = "not_validdd")
        
    elif request.method == "POST":
        def convert(number):     
            romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
            if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
                return "Not Valid Input !!!"
            number = int(number)    
            result = ""
            for key, value in romandict.items():
                while number >= value:
                    quotient = number // value 
                    result += key * quotient
                    number %= value
            return result

        return render_template('result.html',number_roman = convert(num), number_decimal= num, developer_name = "E2248-Muhammet")

    else:
        return render_template("index.html", developer_name = "E2248-Muhammet")




if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)
