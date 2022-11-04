from flask import Flask,render_template

app=Flask(__name__)


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




if __name__ == '__main__':
    app.run(debug=True)


