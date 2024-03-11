# See: https://flask-mysql.readthedocs.io/en/latest/

# Make sure to install the following packages
# pip install flask==2.2.3
# pip install Werkzeug==2.3.7
# pip install flask-mysql


from flask import Flask, jsonify, json
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'meec'
app.config['MYSQL_DATABASE_PASSWORD'] = '00meec'
app.config['MYSQL_DATABASE_DB'] = 'sensors'


# ---------------------------------------
# Initialize MySQL
# ---------------------------------------
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index_mysql():
    # Access MySQL database
    cursor = mysql.get_db().cursor()

    # Example query
    cursor.execute('SELECT * FROM reading')

    # Fetch data and convert to JSON.
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, port=8081)
