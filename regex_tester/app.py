import sys

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from re import match

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = "it's secret"
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regex = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(1024), nullable=False)
    result = db.Column(db.Boolean, nullable=False)

# write your code here
db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        regex = request.form.get('regex')
        text = request.form.get('text')
        if match(regex, text):
            result = True
        else:
            result = False
        test_result = Record(regex=regex, text=text, result=result)
        db.session.add(test_result)
        db.session.commit()
        return redirect(f'/result/{test_result.id}/')
    return render_template("home.html")


@app.route('/history/')
def history():
    records = Record.query.all()
    return render_template('history.html', records=records)


@app.route('/result/<int:id>/')
def show_result(id):
    result = Record.query.filter_by(id=id).first()
    return render_template('result.html', regex=result.regex, text=result.text, result=result.result)



# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
