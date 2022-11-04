from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(50),nullable=False)
    text = db.Column(db.Text,nullable=False)
    category = db.Column(db.String(50),nullable=False)
    price =db.Column(db.Integer,nullable=False)
    isActive =db.Column(db.Boolean,default=True)