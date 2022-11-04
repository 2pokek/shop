from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/create')
def create():
    db.create_all()
    return 'all tables created'


@app.route('/')
def main():
    products= Product.query.order_by(Product.price).all()
    return render_template('main.html',data=products)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/favorite')
def favorite():
    return render_template('favorite.html')


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form['title']
        text = request.form['text']
        category = request.form['category']
        price = request.form['price']

        product = Product(title=title, text=text, category=category, price=price)
        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/')
        except:
            return 'Something went wrong,try again'
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
