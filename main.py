from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import db


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/create')
def create():
    db.create_all()
    return 'all tables created'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

@app.route('/add')
def add():
    return render_template('add.html')



if __name__ == '__main__':
    app.run(debug=True)


