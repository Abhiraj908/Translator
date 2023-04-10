from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweb-data.db'

db = SQLAlchemy()
db.init_app(app)

class LegalModel(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    court_name = db.Column(db.String(100), nullable=False)
    party_name1 = db.Column(db.String(500), nullable=False)
    party_name2 = db.Column(db.String(500), nullable=False)
    order_date = db.Column(db.DateTime, default = datetime.utcnow())
    judges = db.Column(db.String(500), nullable=False)
    held = db.Column(db.DateTime, default = datetime.utcnow())

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # print('Helo world')
    return render_template('index.html')
    
@app.route('/save')
def save():
    return render_template('save_form.html')

# @app.route('/save')
# def save_data():
#     return render_template(url_for('table'))

if __name__ == "__main__":
    app.run(debug=True)