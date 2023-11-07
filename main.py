
#? pip install flask flask-pymongo
from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    mongo.db.inventory.insert_one({"b":31})
    a = mongo.db.inventory.find({})
    return render_template('index.html',data=a)

@app.route('/mydata')
def mydata():
    info = ['Vedant', 'Age: 19', 'Programmer', 'Music Lover']
    return render_template('mydata.html', personal=info)

app.run(debug=True,port=3000)