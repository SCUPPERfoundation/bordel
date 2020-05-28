import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    DBHOST = os.environ.get('POSTGRES_POSTGRESQL_SERVICE_HOST')
    DBPASS = os.environ.get('PGPASSWORD')
    DBURI = 'postgresql://postgres:'+DBPASS+'@'+DBHOST+'/'+__name__
    app.config['SQLALCHEMY_DATABASE_URI'] = DBURI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
