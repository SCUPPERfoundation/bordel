import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

"""
try:
    DBHOST = os.environ.get('POSTGRES_POSTGRESQL_SERVICE_HOST')
    DBPASS = os.environ.get('PGPASSWORD')
    DBURI = 'postgresql://postgres:'+DBPASS+'@'+DBHOST+'/'+__name__
    app.config['SQLALCHEMY_DATABASE_URI'] = DBURI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
except:
    pass
"""

#app.config.from_object('bordel.default_settings')
os.environ['BORDEL_SETTINGS'] = os.environ.get('BORDEL_SETTINGS', '.bordelrc')
app.config.from_envvar('BORDEL_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DBURI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if app.config['DEBUG']:
    try:
        from flask.ext.debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)
    except:
        pass

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.before_first_request
def before_first_request():
    try:
        db.create_all()
    except Exception as e:
        app.logger.error(str(e))

from . import routes
