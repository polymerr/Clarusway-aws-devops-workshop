from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first conditional experience in Flask"
    return render_template("index.html", mesaj = first)  # Burada msjı silersek else condition çalışır (index.html'deki)

@app.route("/sec")
def for_structure():
    names = ["muhammet", "feyzullah", "serdar", "bülent"]

    return render_template("deneme.html", isimler = names)




if __name__ == "__main__":
    app.run(debug=True)