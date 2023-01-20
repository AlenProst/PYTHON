from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from models import db, User
import msal
import requests
import json
from my_user import token_creation, create_user_in_office, delete_user_graph


app = Flask (__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)



@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/create_user/', methods=['POST','GET'])
def create_user():
    if request.method == 'POST':
        user_dispayName = request.form['displayname']
        user_domain= request.form['domain']
        upn = user_dispayName + "@" + user_domain

        access_token = token_creation()

        create_user_in_office(user_dispayName,user_domain,access_token)

        task_content = request.form['displayname']
        task_upn = upn
        new_task = User(content=task_content, upn=task_upn)


        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect('/create_user/')
        except:
            return upn


        


     
    else:
        tasks = User.query.order_by(User.date_created).all()
        return render_template('create_user.html', tasks=tasks)


@app.route('/delete/<int:id><tupn>')
def delete(id,tupn):
    task_to_delete = User.query.get_or_404(id)
    access_token = token_creation()
    delete_user_graph(tupn,access_token)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/create_user/')
    except:
        return 'There was a problem deleting that user'



@app.route('/create_group/')
def create_group():
    return render_template('create_group.html')


@app.route('/createdatabase/')
def create():
    db.create_all()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)