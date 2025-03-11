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


# Example of a custom encoder subclassing JSONEncoder - this is necessary to handle the ObjectId type
class MongoJsonEncoder(json.JSONEncoder):
    """JSON encoder for Mongo ObjectID.
    if the object is an ObjectId, it will be converted to a string.
    If the object is not an ObjectId, it will call the default JSON encoder.
    """
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

# Set the custom encoder as the default encoder for the app
app.json_encoder = MongoJsonEncoder


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
