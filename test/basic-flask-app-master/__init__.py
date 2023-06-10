from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from multiplier_quiz import *
from flask import Flask, render_template, request

app = Flask(__name__)

#202212
#from flask import session
#from flask_session import Session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
#db = "dbname='bank' user='postgres' host='127.0.0.1' password = 'UIS'"
db = "dbname='postgres' user='postgres' host='localhost' password = ''"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'