from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')


@app.route("/about")
def gaurav():
    name = "myflask"
    return render_template('about.html', name2=name)


# app.run(debug=True)
print(__name__)
print(type(__name__))
