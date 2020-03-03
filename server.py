from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title_name=title)


@app.route('/training/<prof>')
def profession(prof):
    return render_template("training.html", prof=prof.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
