from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for,session, flash
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask (__name__)
app.config['SECRET_KEY'] = 'your secret key'

database = 'mydb'
username = "user1"
password = "1"
server = "192.168.1.25"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user1:1@192.168.1.25:3306/mydb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class German_Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<case {self.id}>'

@app.route('/')
def index():

    case = German_Case.query.all()
    return render_template('index.html', case=case)


@app.route('/<int:case_id>/',methods=('GET', 'POST'))
def case(case_id):
    case = German_Case.query.get_or_404(case_id)
    return render_template('case.html', case=case)


@app.route('/<int:case_id>/edit/', methods=('GET', 'POST'))
def edit(case_id):
    my_case_new = German_Case.query.get_or_404(case_id)

    if request.method == 'POST':
        case = request.form['case']

        my_case_new.case = case
        


        db.session.add(my_case_new)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', case=my_case_new)



@app.route('/test/', methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        case_value = request.form['value']
        article = request.form['article']
        adj = request.form['adj']
        noun = request.form['noun']
        case_id = request.form['case_id']

        word_to_compare = article + " " + adj + " " + noun

        if word_to_compare.strip().lower() == case_value.strip().lower():
            case_to_delete = German_Case.query.get_or_404(case_id)
            db.session.delete(case_to_delete)
            db.session.commit()
            return redirect(url_for('index'))
     


        else:

            flash("Try Again")
            case = German_Case.query.get_or_404(case_id)
            return render_template('case.html', case=case)
    



@app.post('/<int:case_id>/delete/')
def delete(case_id):
    case_to_delete = German_Case.query.get_or_404(case_id)
    db.session.delete(case_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)