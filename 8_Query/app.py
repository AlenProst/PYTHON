from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for,session, flash
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from models import db, MyPrepositionCaseTable, db2, TenseTest
from filldb import fill_db
import random
from sqlalchemy import func

app = Flask (__name__)
app.config['SECRET_KEY'] = 'your secret key'

database = 'mydb'
username = "user1"
password = "1"
server = "192.168.1.39"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user1:1@192.168.1.42:3306/mydb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
db2.init_app(app)


numbers = list(range(1,1276))
# numbers = list(range(676,1276)) - ACC Numbers


prep_numbers = list(range(1,11))
selected_ids = []

@app.route('/createdatabase/')
def createdatabase():
    db.create_all()
    return redirect('/')

    

@app.route('/testtense/', methods=('GET', 'POST'))
def testtense():

    count = db.session.query(func.count(TenseTest.id)).scalar()
    random_row_num = random.randint(0, count - 1)

    random_row = db.session.query(TenseTest).offset(random_row_num).first()   
    return render_template('3_testtense.html', words=random_row)

@app.route('/answer/', methods=('GET', 'POST'))
def answer():

    if request.method == 'POST':
        answer= request.form['answer-input']
        sentence_from_hidden = request.form['hidden_sentence']
        hidden_id = int(request.form['hidden_id'])

        if answer.lower().strip() == sentence_from_hidden.lower().strip():


            count = db.session.query(func.count(TenseTest.id)).scalar()

            while True:


                random_row_num = random.randint(0, count - 1)


                random_row = db.session.query(TenseTest).offset(random_row_num).first()

                if random_row.id not in selected_ids:
                    selected_ids.append(random_row.id)
                    return render_template('3_testtense.html', words=random_row)
 

            

        else:
            
            random_row_num = hidden_id
            random_row = TenseTest.query.get_or_404(random_row_num)
            return render_template('3_testtense.html', words=random_row)





        



if __name__ == "__main__":
    app.run(debug=True)



