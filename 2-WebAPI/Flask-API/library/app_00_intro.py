#!flask/bin/python

# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask

# Next we create an instance of this class. The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example), you should use __name__ because depending on if it’s started
# as application or imported as module the name will be different ('__main__' versus the actual import name).
# This is needed so that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__)

# route() decorator tells Flask what URL should trigger our function.
@app.route('/iot/api/v1.0/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)