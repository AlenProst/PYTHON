
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class MyPrepositionCaseTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preposition = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(200), nullable=True)
    prep = db.Column(db.String(200), nullable=True)
    pronoun = db.Column(db.String(200), nullable=True)
    adj = db.Column(db.String(200), nullable=True)
    noun = db.Column(db.String(200), nullable=True)
    pronoun_form = db.Column(db.String(200), nullable=True)
    adj_form = db.Column(db.String(200), nullable=True)
    edit_field = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        return '<Task %r>' % self.id

db2 = SQLAlchemy()
class TenseTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tense = db.Column(db.String(200), nullable=True) 
    content = db.Column(db.String(200), nullable=True)
    el1 = db.Column(db.String(200), nullable=True)
    el2 = db.Column(db.String(200), nullable=True)
    el3 = db.Column(db.String(200), nullable=True)
    el4 = db.Column(db.String(200), nullable=True)
    el5 = db.Column(db.String(200), nullable=True)
    el6 = db.Column(db.String(200), nullable=True)
    translation = db.Column(db.String(200), nullable=True)

   
    def __repr__(self):
        return '<Task %r>' % self.id