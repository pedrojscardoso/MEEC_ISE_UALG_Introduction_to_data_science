# See: https://pymongo.readthedocs.io/en/stable/
#
# Make sure to install the following packages:
#   pip install flask
#   pip install pymongo


from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# -------------------------------------------------------------------
# CONNECTION POOLING (Automatic in PyMongo)
# -------------------------------------------------------------------
# Unlike MySQL, where we had to manually create a connection pool,
# PyMongo's MongoClient HAS BUILT-IN CONNECTION POOLING.
#
# We instantiate 'client' once at the top level when the app starts.
# Every time a Flask route runs, PyMongo automatically borrows a 
# connection from its internal pool, and returns it when done.
# 
# Best practice: NEVER create a new MongoClient inside an @app.route!
# -------------------------------------------------------------------
MONGO_URI = 'mongodb://localhost:27017/'
client = MongoClient(MONGO_URI)

# Select the database and collection - this can also be inside the route
db = client['sensorsDB']
collection = db['sensors_readings']


@app.route('/', methods=['GET'])
def index_mongo():
    # Fetch all documents from the collection
    cursor = collection.find({})

    # Convert the cursor to a list of dictionaries
    data = list(cursor)

    # ---------------------------------------------------------------
    # HANDLING MONGODB ObjectIds
    # ---------------------------------------------------------------
    # MongoDB documents automatically have an '_id' field of type 'ObjectId'.
    # Flask's built-in jsonify() DOES NOT know how to turn an ObjectId 
    # into JSON, and will crash with a TypeError if we don't convert it.
    # 
    # Solution: Convert the ObjectId back to a string before JSONifying.
    # ---------------------------------------------------------------
    for document in data:
        if '_id' in document:
            document['_id'] = str(document['_id'])

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
