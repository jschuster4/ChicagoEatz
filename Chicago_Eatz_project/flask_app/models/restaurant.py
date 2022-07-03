from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user



class Restaurant:
    def __init__(self,data): 
        self.id = data['id']
        self.name = data['name']
        self.cuisine = data['cuisine']
        self.rating = data['rating']
        self.casual = data['casual']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.description = data['description']
        self.address = data['address']
        self.user = {}

    @classmethod
    def get_all_restaurants(cls):
        query = "SELECT * FROM restaurants"
        results = connectToMySQL('dining_schema').query_db(query)
        restaurants = []
        for item in results: 
            restaurants.append( cls(item) )
        return restaurants

    @classmethod
    def add_restaurant(cls, data):
        query = "INSERT INTO restaurants (name, cuisine, rating, casual, created_at, updated_at, user_id, description, address) VALUES(%(name)s, %(cuisine)s, %(rating)s, %(casual)s, NOW(), NOW(), %(id)s, %(description)s, %(address)s);"
        results = connectToMySQL('dining_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_restaurant(data):
        is_valid = True

        # confirm that the first name length is between 3 and 99 characters
        if len(data["name"]) < 3 or len(data['name']) > 99:
            is_valid = False
            flash("title must be at least 3 characters, but no longer than 99 characters")

        # confirm that the last name length is between 1 and 500 characters
        if len(data["description"]) < 1 or len(data["description"]) > 499:
            is_valid = False
            flash("Description must not be left blank, but no longer than 500 characters")

        if data["rating"] == "": 
            is_valid = False
            flash("There must be a rating entered")
        
        if data["cuisine"] == "": 
            is_valid = False
            flash("There must be a cuisine type entered")
        
        if data["casual"] == "": 
            is_valid = False
            flash("There must be a casual rating entered. ")

        if data["address"] == "":
            is_valid = False
            flash("There must be an address entered")

        return is_valid

    @classmethod
    def get_one_restaurant(cls,data): 
        query = "SELECT * FROM restaurants WHERE id= %(id)s;"
        results = connectToMySQL('dining_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def delete_restaurant(cls, data):
        query = "DELETE FROM restaurants WHERE id = %(id)s;"
        results = connectToMySQL('dining_schema').query_db(query, data)

    @classmethod
    def update_restaurant(cls, data):
        query = "UPDATE restaurants SET name = %(name)s, cuisine = %(cuisine)s, rating = %(rating)s, description = %(description)s, updated_at = NOW(), casual = %(casual)s, address = %(address)s WHERE id= %(id)s"
        results = connectToMySQL('dining_schema').query_db(query, data)
        # dont return anything for update or delete

    @classmethod
    def get_one_restaurant_with_user(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN users ON users.id = restaurants.user_id WHERE restaurants.id= %(id)s;"
        results = connectToMySQL('dining_schema').query_db(query, data)
        restaurant = cls(results[0])
        user_data = {
            'id' : results[0]["users.id"],
            'first_name' : results[0]["first_name"],
            'last_name' : results[0]["last_name"],
            'email' : results[0]["email"],
            'password' : results[0]["password"],
            'created_at' : results[0]["users.created_at"],
            'updated_at' : results[0]["users.updated_at"],
        }
        restaurant.user = user.User(user_data)
        return restaurant