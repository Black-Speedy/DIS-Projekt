from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt

#202212
#from flask import session
#from flask_session import Session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
#db = "dbname='bank' user='postgres' host='127.0.0.1' password = 'UIS'"
db = "dbname='postgres' user='postgres' host='localhost' password = '0301'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

