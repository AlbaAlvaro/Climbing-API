from flask import Flask, render_template, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017") #host uri  
db = client["climbing-api"] #Select the database  

# app.config["MONGO_URI"] = "mongodb://localhost:27017/climbing-api"
# mongo = PyMongo(app)

# Display home
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/', methods=[ "POST"])
def index_post():
    zona = request.form['area']
    nivel = request.form['nivel']
    popu = request.form['popu']
    print(type(nivel))
    if nivel=="Select a grade" and popu=="Select the popularity":
        result=db[zona].find({},{"_id":0})
        return  render_template("list.html", task = list(result))
    elif popu=="Select the popularity":
        result=db[zona].find({"grade": nivel}, {"_id":0, "route name":1, "grade":1}).limit(10)
        return  render_template("list.html", task = list(result)) 
    else:
        result=db[zona].find({"grade":nivel}, {"_id":0, "route name":1, "grade":1}).sort("ascents",-1).limit(10)
        return  render_template("list.html", task = list(result))
    return "Select an option"


@app.route("/route/place")
def routePlace():
    # get collection
    route = list(db[collection].find({}, {"_id":0, "route name":1, "grade":1, "sector":1}))
    return render_template("routeplace.html", dumps(route[:5]))

@app.route("/route/place/grade")
def routeGrade():
    # get grade, collection
    route = list(db[collection].find({"grade": grade}, {"_id":0, "route name":1}))
    return dumps(route[:5])

@app.route("/route/place/sector/grade")
def routeSectorGrade(grade, sector, collection):
    route=list(db[collection].find({"grade":grade, "sector name": sector}, {"_id":0, "route name":1}))
    return dumps(route[:10])

@app.route("/route/place/sector/grade/popular")
def PopularRoute(grade, sector, collection):
    route=list(db[collection].find({"grade":grade, "sector name": sector}, {"_id":0, "route name":1}).sort("ascents",-1).limit(5))
    return dumps(route)



