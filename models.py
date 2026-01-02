from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy ( )

class Player ( db.Model ):
	id = db.Column ( db.Integer, primary_key = True )
	first_name = db.Column ( db.String ( 20 ), nullable = False )
	last_name = db.Column ( db.String ( 20 ), nullable = False )
	phone = db.Column ( db.Integer )
	marks = db.Column ( db.Integer )
	payment_mode = db.Column ( db.String ( 10 ) )
