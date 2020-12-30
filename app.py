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
        meals = {
            "meal_name": request.form.get("meal_name"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions")
        }
        mongo.db.meals.insert_one(meals)
        flash("Thank you for adding your meal")
        return redirect(url_for("get_meals"))

    meals = mongo.db.meals.find().sort("meal_name", 1)
    return render_template("add_meal.html", meals=meals)

@app.route("/edit_meal/<meals_id>", methods=["GET", "POST"])
def edit_meal(meals_id):
    meals = mongo.db.meals.find_one({"_id": ObjectId(meals_id)})
    meals = mongo.db.meals.find().sort("meal_name", 1)
    return render_template("edit_meal.html", meals=meals)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)