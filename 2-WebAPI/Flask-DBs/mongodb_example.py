# See: https://flask-pymongo.readthedocs.io/en/latest/

# Make sure to install the following packages
# pip install flask==2.2.3
# pip install Werkzeug==2.3.7
# pip install Flask-PyMongo


from flask import Flask, jsonify, json
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)


# configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/sensorsDB'

# ---------------------------------------
# Initialize MongoDB
# ---------------------------------------
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def index_mongo():
    # Access MongoDB collection
    collection = mongo.db.sensors_readings

    # Example query
    cursor = collection.find({})

    # Fetch data and convert to JSON
    data = list(cursor)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
