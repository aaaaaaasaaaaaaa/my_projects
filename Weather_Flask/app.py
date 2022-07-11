import sys
import requests
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, redirect, flash, get_flashed_messages


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY'] = "it's secret"
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    weather = db.Column(db.String(30), nullable=False)
    temperature = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.name}'  # , {self.weather}, {self.temperature}'

db.create_all()


@app.route('/', methods=['POST', 'GET'])
def add_city():
    if request.method == 'POST':
        check = False
        while not check:
            cities = City.query.all()
            city_name = request.form.get('city_name')
            api_key = '21dd471facf89f3a8a9b65fb629bdd20'
            api_url = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city_name, api_key))
            api_j = api_url.json()
            # result = json.dumps(api_j)
            if api_j['cod'] == 200:
                for city in cities:
                    if city_name == city.name:
                        check = True
                if check:
                    flash("The city has already been added to the list!")
                    return redirect('/')
                our_city = City(name=city_name, weather=api_j['weather'][0]['main'], temperature=api_j['main']['temp'])
                db.session.add(our_city)
                db.session.commit()
                check = True
            else:
                flash("The city doesn't exist!")
                check = True
        return redirect('/')

                # city=api_j['name'], temperature=api_j['main']['temp'],
                # weather=api_j['weather'][0]['main']
    return render_template('index.html', cities=City.query.all())
# api key - 21dd471facf89f3a8a9b65fb629bdd20


@app.route('/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run(debug=True)
