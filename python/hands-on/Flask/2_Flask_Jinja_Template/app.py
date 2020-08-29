from flask import Flask, render_template #render template de yeni bir kütüphane, onu da import 
#ederek html dosyalarını çalıştırabiliyoruz.

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 12, number2= 24)  # yukarıda render template'i import ettiğim için index.html'i
# çağırabiliyorum.

@app.route("/ikinci")
def second():
    return render_template("yeni.html")



if __name__ == "__main__":
    app.run(debug = True)