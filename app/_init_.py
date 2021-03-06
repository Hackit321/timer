from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)






if __name__ == '__main__':
	app.run(debug=True)