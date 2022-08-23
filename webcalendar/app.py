import sys
from flask import Flask, jsonify, abort
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, reqparse, inputs, Resource
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
app.config['JSON_SORT_KEYS'] = False
api = Api(app)


class EventSchema(Schema):
    id = fields.String()
    event = fields.String()
    date = fields.Date()


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)
db.create_all()





class EventResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_time',
                            type=inputs.date,
                            help='The event date with the correct format is required! The correct format is YYYY-MM-DD!'
                            )

        parser.add_argument('end_time',
                            type=inputs.date,
                            help='The event date with the correct format is required! The correct format is YYYY-MM-DD!'
                            )

        args = parser.parse_args(strict=True)
        schema = EventSchema(many=True)
        if args['start_time'] and args['end_time']:
            events = Event.query.filter(Event.date.between(args['start_time'], args['end_time']))
            return jsonify(schema.dump(events))
        all_events = Event.query.all()
        return jsonify(schema.dump(all_events))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('event',
                            type=str,
                            help='The event name is required!',
                            required=True)
        parser.add_argument('date',
                            type=inputs.date,
                            help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
                            required=True)
        args = parser.parse_args(strict=True)
        event_to_add = args['event']
        date_to_add = args['date']
        db.session.add(Event(event=event_to_add, date=date_to_add))
        db.session.commit()
        parser.remove_argument("event")
        parser.remove_argument("date")
        return jsonify(
            {
                "message": "The event has been added!",
                "event": event_to_add,
                "date": date_to_add.strftime('%Y-%m-%d')
            })


class EventToday(Resource):
    def get(self):
        schema = EventSchema(many=True)
        events = Event.query.filter(Event.date == date.today())
        return jsonify(schema.dump(events))


class EventByID(Resource):
    def get(self, id):
        event = Event.query.filter_by(id=id).first()
        if event is None:
            return abort(404, "The event doesn't exist!")
        return jsonify(
            {
                "id": event.id,
                "event": event.event,
                "date": event.date.strftime('%Y-%m-%d')
            })

    def delete(self, id):
        event = Event.query.filter_by(id=id).first()
        if event is None:
            return abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return jsonify(
            {
                "message": "The event has been deleted!"
            })


api.add_resource(EventByID, '/event/<int:id>')
api.add_resource(EventResource, '/event')
api.add_resource(EventToday, '/event/today')


# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run(debug=True)
