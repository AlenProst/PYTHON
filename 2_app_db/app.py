from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flaskext.mysql import MySQL





app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypass@mariadbtest:3306/mydb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user1:1@192.168.0.183:3306/mydb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_db = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Note %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        note_back_end= request.form["the_note_entered_in_form"]
        note_to_be_added_in_db = Note(note_db=note_back_end)

        db.session.add(note_to_be_added_in_db)
        db.session.commit()
        return redirect('/')

    else:
        notes_saved = Note.query.order_by(Note.date_created).all()
        return render_template("index.html", notes_saved = notes_saved)


@app.route("/delete/<int:id>")
def delete(id):
    note_to_delete = Note.query.get(id)
    db.session.delete(note_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    note_to_update = Note.query.get_or_404(id)

    if request.method=="POST":
        note_to_update.note_db = request.form['content']    
        db.session.commit()
        return redirect('/')

    else:
        return render_template("update.html", note_to_update = note_to_update.id, note_to_update1 = note_to_update.note_db)

       


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,host = '0.0.0.0')