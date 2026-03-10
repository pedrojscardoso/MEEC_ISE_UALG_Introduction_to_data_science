"""
Example 1: Basic Flask Routing
This is the simplest form of a Flask route. It returns plain text.
"""
from app import app

# The @app.route decorator maps a URL path to a Python function.
# Here we map both the root URL ('/') and the '/index' URL to the same function.
@app.route('/')
@app.route('/index')
def index():
    # The return value is sent back to the client's browser.
    return "Hello, World!"
