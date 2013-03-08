from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'pope_picker'}
app.config['SECRET_KEY'] = '09443jlkdjf0f9490j3f8j4afj9aj90j3'

db = MongoEngine(app)


def register_blueprints(app):
    from popepicker.views import popes
    app.register_blueprint(popes)

register_blueprints(app)


if __name__ == '__main__':
    app.run()
