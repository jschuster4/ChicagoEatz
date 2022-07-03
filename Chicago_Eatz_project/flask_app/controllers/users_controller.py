from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt 
from flask_app.models.user import User
from flask_app.models.restaurant import Restaurant

bcrypt = Bcrypt(app)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/users/register", methods = ['POST'])
def register_user():
    if User.validate_user(request.form):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        User.create_user(data)
    return redirect("/")

@app.route("/users/login", methods = ['POST'])
def login_user(): 
    users = User.get_user_by_email(request.form)
    if len(users) != 1: 
        flash("Incorrect username")
        return redirect("/")
    user = users[0]
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password")
        return redirect("/")

    session['user_id'] = user.id
    session['email'] = user.email
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name

    return redirect("/success")

@app.route("/success")
def success(): 
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        'id' : session['user_id']
    }
    # getting an error when there is no entries for food in the database
    # one_user = User.get_user_shows(data)
    all_restaurants = Restaurant.get_all_restaurants()
    return render_template("user_page.html", all_restaurants = all_restaurants)

@app.route("/logout")
def logout(): 
    session.clear()
    return redirect("/")

# @app.route("/shows/<int:show_id>")
# def view_show(show_id):
#     if 'user_id' not in session:
#         flash("You must be logged in to view this page")
#         return redirect("/")
#     data = {
#         'id' : show_id
#     }
#     user = User.get_one_show_with_user(data)
#     return render_template("show_instance.html", user = user)

