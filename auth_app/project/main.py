from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
import sqlite3


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile(): # sqlite studio
    try:   
        connection = sqlite3.connect('mydatabase.db')
        cur = connection.cursor()
        cur.execute("INSERT INTO node01 (temp, hum) VALUES (?, ?)",
                    (request.args.get('temperature1'), request.args.get('humidity1'))
                    )

        cur.execute("INSERT INTO node02 (temp, hum) VALUES (?, ?)",
                    (request.args.get('temperature2'), request.args.get('humidity2'))
                    )

        cur.execute("INSERT INTO node03 (temp, hum) VALUES (?, ?)",
                    (request.args.get('temperature3'), request.args.get('humidity3'))
                    )

        cur.execute("INSERT INTO node04 (temp, hum) VALUES (?, ?)",
                    (request.args.get('temperature4'), request.args.get('humidity4'))
                    )

        connection.commit()
        connection.close()
        flash('Data was successfully inserted!')
    except Exception as exc:
        print ("Can't upload because %s" % exc)
    return render_template('profile.html', name=current_user.name,temperature1 = request.args.get('temperature1'), humidity1 = request.args.get('humidity1'), temperature2 = request.args.get('temperature2'), humidity2 = request.args.get('humidity2'),
                           temperature3 = request.args.get('temperature3'), humidity3 = request.args.get('humidity3'),
                           temperature4 = request.args.get('temperature4'), humidity4 = request.args.get('humidity4'))