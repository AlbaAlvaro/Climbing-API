from flask import Flask, render_template, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
app = Flask(__name__)

app.static_folder = 'static'
app._static_folder = 'static'

print(app.static_url_path)
print(app.template_folder)
print(app._static_folder)
print(app.static_folder)

client = MongoClient("mongodb://127.0.0.1:27017") #host uri  
db = client["climbing-api"] #Select the database  


# Display home
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/', methods=[ "POST"])
def index_post():
    zona = request.form['area']
    nivel = request.form['nivel']
    if nivel=="Select a grade":
        result=db[zona].find({},{"_id":0})
        return render_template("list.html", task = list(result) )

    elif zona=="Select an area in Spain":
        return render_template("index.html")

    elif zona!="Select an area in Spain" and nivel!="Select a grade":
        grado=db[zona].find_one({},{"_id":0,"grade":1})
        if (grado["grade"][1]).islower():
            try:
                letra=nivel[1].lower()         
                nivel=nivel[0]+letra+nivel[2]
            except Exception:
                letra=nivel[1].lower()         
                nivel=nivel[0]+letra
        result=db[zona].find({"grade": nivel}, {"_id":0}).limit(10)
        return render_template("list.html", task = list(result))

    else:
        print("a")
        return render_template("index.html")

