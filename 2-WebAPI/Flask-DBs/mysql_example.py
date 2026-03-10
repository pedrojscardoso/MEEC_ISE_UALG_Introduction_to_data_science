# See: https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html
#
# Make sure to install the following packages:
#   pip install flask
#   pip install mysql-connector-python


from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'meec',
    'password': '00meec',
    'database': 'sensors'
}

# -------------------------------------------------------------------
# CONNECTION POOLING (Best Practice for APIs)
# -------------------------------------------------------------------
# Creating a database connection from scratch on every HTTP request 
# is very slow and uses up database resources quickly. 
# 
# Instead, we create a "Connection Pool" when the app starts.
# The pool creates a set number of background database connections 
# holding them open. When an API route is called, it "borrows" a 
# connection from the pool.
# -------------------------------------------------------------------
db_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,             # Keep 5 connections open at all times
    pool_reset_session=True, # Reset session variables when returning connection
    **MYSQL_CONFIG
)


@app.route('/', methods=['GET'])
def index_mysql():
    
    # 1. Borrow a connection from the pool (virtually instant)
    connection = db_pool.get_connection()

    try:
        # Create a cursor that returns rows as dictionaries instead of tuples
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM reading')

        # Fetch data
        data = cursor.fetchall()
        cursor.close()
    finally:
        # 2. Return the connection to the pool.
        # Note: Because this connection came from a pool, calling .close()
        # does NOT kill the connection to the database. It just releases it 
        # back into the pool so the next HTTP request can use it.
        connection.close()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8081)
