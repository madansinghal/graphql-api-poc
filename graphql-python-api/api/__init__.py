from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nunaoztj:HfpP6YLR33rOqWJ5Sngbuv1NRNRiXE_c@tuffi.db.elephantsql.com/nunaoztj"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)





@app.route('/')
def hello():
    return 'My First API !!'
