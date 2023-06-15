import os
import flask
from tabledef import *
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

from calculator.functions import Define_FUC, load_model
from handlers.routes import configure_routes

engine = create_engine('sqlite:///login_db.db?check_same_thread=False', echo=True)
Session = sessionmaker(bind=engine)

load_model()
Define_FUC(Session)

application = flask.Flask(__name__)
application.secret_key = 'web_app_for_face_recognition_and_liveness'
CORS(application)
configure_routes(application, Session)

if __name__ == "__main__":
    application.run(host = '0.0.0.0', port = '8080', debug = True)
    # application.run()