"""
Example 2: Returning Inline HTML
This example demonstrates returning actual HTML code directly from a Python string.

NOTE: This is considered BAD PRACTICE because it mixes application logic
(Python) with presentation logic (HTML), making the code hard to maintain.
For proper separation of concerns, we should use Templates (see routes3.py).
"""
from app import app

# Mock data
things = [{'id': 1, 'name': 'Prometheus'}]

@app.route('/')
@app.route('/index')
def index():
    # Returning a hardcoded HTML string built via concatenation
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Thing: ''' + things[0]['name'] + '''!</h1>
            </body>
        </html>'''
