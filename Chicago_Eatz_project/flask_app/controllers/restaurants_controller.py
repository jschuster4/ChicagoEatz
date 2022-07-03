import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.restaurant import Restaurant
import os
import requests

@app.route("/restaurant/create")
def display_new_show_page(): 
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    return render_template("create_restaurant.html")

@app.route("/restaurant/new", methods= ['POST'])
def add_restaurant(): 
    if Restaurant.validate_restaurant(request.form):
        data = {
            'name' : request.form['name'],
            'cuisine' : request.form['cuisine'],
            'rating' : request.form['rating'],
            'description' : request.form['description'],
            'id' : session['user_id'],
            'casual' : request.form['casual'],
            'address' : request.form['address'],
        }
        new_restaurant = Restaurant.add_restaurant(data)
        return redirect("/success")
    else: 
        return redirect("/shows/create")

# @app.route("/restaurants/view/<int:restaurant_id>")
# def view_one_restaurant(restaurant_id):
#     if 'user_id' not in session:
#         flash("You must be logged in to view this page")
#         return redirect("/")
#     data = {
#         'id' : restaurant_id
#     }
#     one_restaurant = Restaurant.get_one_restaurant(data)
#     return render_template("view_restaurant.html", one_restaurant = one_restaurant)


@app.route("/restaurants/delete/<int:restaurant_id>")
def delete_show(restaurant_id):
    data = {
        'id' : restaurant_id
    }
    Restaurant.delete_restaurant(data)
    return redirect('/success')

@app.route("/restaurants/update/<int:restaurant_id>")
def show_edit_page(restaurant_id):
    data = {
        'id' : restaurant_id
    }
    one_restaurant = Restaurant.get_one_restaurant(data) 
    return render_template("edit_restaurant.html", one_restaurant = one_restaurant)

@app.route("/restaurants/edit/<int:restaurant_id>", methods = ['POST'])
def update_show(restaurant_id):
    if Restaurant.validate_restaurant(request.form):
        data = {
            'name' : request.form['name'],
            'cuisine' : request.form['cuisine'],
            'rating' : request.form['rating'],
            'description' : request.form['description'],
            'casual' : request.form['casual'],
            'address' : request.form['address'],
            'id' : restaurant_id,
        }
        Restaurant.update_restaurant(data)
        return redirect("/success")
    else: 
        return redirect(f"/restaurants/edit/{restaurant_id}")

@app.route("/restaurants/view/<int:restaurant_id>")
def view_one_review_with_user(restaurant_id):
    data = {
        'id' : restaurant_id
    }
    one_restaurant = Restaurant.get_one_restaurant_with_user(data)
    return render_template("view_restaurant.html", one_restaurant = one_restaurant)
