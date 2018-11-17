from flask import Flask, render_template, json
from flask_pymongo import PyMongo

# init app and database
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# provide the websites
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/test')
def test():
    my_dict = { "data" : [
          { "id":1, "name":"John",  "createdAt": '201-10-31:9: 35 am',"keywords": 0.03343 },
          { "id":2, "name":"Jane",  "createdAt": '2011-10-31', "keywords": 0.03343 },
          { "id":3, "name":"Susan", "createdAt": '2011-10-30', "keywords": 0.03343 },
          { "id":4, "name":"Chris", "createdAt": '2011-10-11', "keywords": 0.03343 },
          { "id":5, "name":"Dan",   "createdAt": '2011-10-21', "keywords": 0.03343 },
          { "id":6, "name":"John",  "createdAt": '2011-10-31', "keywords": 0.03343 },
          { "id":7, "name":"Jane",  "createdAt": '2013-09-21' },
          { "id":8, "name":"Susan", "createdAt": '2013-10-31', "keywords": ["Susan", "Abc"] },
        ] }
    return json.dumps(my_dict)

# main method for easy use within the  commandline
if __name__ == "__main__":
    # enable debug mode only for developement
    app.run(debug=True)