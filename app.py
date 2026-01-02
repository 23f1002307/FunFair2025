from flask import Flask, render_template, request, redirect, url_for
from models import Player, db

app = Flask ( __name__ )
app.config [ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///fun_fair.db"
db.init_app ( app )

with app.app_context ( ):
	db.create_all ( )

@app.route ( "/", methods = [ "GET", "POST" ] )
def index ( ):
	if request.method == "POST":
		first_name = request.form.get ( "first_name" )
		last_name = request.form.get ( "last_name" )
		contact_number = request.form.get ( "contact_number" )
		payment_mode = "pending"
		new_player = Player ( first_name = first_name, last_name = last_name, phone = contact_number, marks = 0, payment_mode = payment_mode )
		db.session.add ( new_player )
		db.session.commit ( )
		return redirect ( url_for ( 'leader_board' ))
	return render_template ( "index.html" )

@app.route ( "/leader_board", methods = [ "GET", "POST" ] )
def leader_board ( ):
	all_players = Player.query.order_by ( Player.marks.desc ( )).all ( )
	return render_template ( "leader_board.html", all_players = all_players )

@app.route ( "/update/payment_mode/<int:player_id>/<mode>", methods = [ "GET", "POST" ] )
def update_payment_mode ( player_id, mode ):
	player = Player.query.get ( player_id )
	player.payment_mode = mode
	db.session.commit ( )
	return redirect ( url_for ( 'leader_board' ))

@app.route ( "/update_marks/<int:player_id>", methods = [ "GET", "POST" ] )
def update_marks ( player_id ):
	player = Player.query.get ( player_id )
	marks = request.form.get ( "marks" )
	player.marks = marks
	db.session.commit ( )
	return redirect ( url_for ( "leader_board" ))

if __name__ == "__main__":
	app.run ( debug = True )