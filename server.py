from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    title="Index"
    return render_template("index.html",title=title)


@app.route("/galeri")
def galeri():
    title="Galeri"
    return render_template("galeri.html",title=title)
    

if __name__ == '__main__':
    app.run(debug=True)
