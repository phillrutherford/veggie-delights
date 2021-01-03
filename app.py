import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


print(app.config["MONGO_URI"])

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_meals")
def get_meals():
    meals = list(mongo.db.meals.find())
    return render_template("meals.html", meals=meals)


@app.route("/add_meal", methods=["GET", "POST"])
def add_meal():
    if request.method == "POST":
        meal = {
            "meal_name": request.form.get("meal_name"),
            "meal_ingredients": request.form.get("meal_ingredients"),
            "meal_instructions": request.form.get("meal_instructions")
        }
        mongo.db.meals.insert_one(meal)
        flash("Thank you for adding your meal")
        return redirect(url_for("get_meals"))

    meals = mongo.db.meals.find().sort("meal_name", 1)
    return render_template("add_meal.html", meals=meals)

@app.route("/edit_meal/<meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    if request.method == "POST":
        update = {
            "meal_name": request.form.get("meal_name"),
            "meal_ingredients": request.form.get("meal_ingredients"),
            "meal_instructions": request.form.get("meal_instructions")
        }
        mongo.db.meals.update({"_id": ObjectId(meal_id)}, update)
        flash("Meal updated succesfully!")
        return redirect(url_for("get_meals"))
    meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    meals = mongo.db.meals.find().sort("meal_name", 1)
    return render_template("edit_meal.html", meals=meals, meal=meal)

@app.route("/delete_meal/<meal_id>")
def delete_meal(meal_id):
    mongo.db.meals.remove({"_id": ObjectId(meal_id)})
    flash("Meal Deleted Succesfully")
    return redirect(url_for("get_meals")) 

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)