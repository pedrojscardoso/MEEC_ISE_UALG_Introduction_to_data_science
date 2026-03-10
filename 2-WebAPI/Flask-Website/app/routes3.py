"""
Example 3: Introduction to Templates (Jinja2)
This example shows the PROPER way to return HTML. Instead of hardcoding 
HTML in Python, we use 'render_template' to load an HTML file (from the 
'templates' folder) and inject Python variables into it.
"""
from flask import render_template
from app import app

# Mock data
things = [{'id': 1, 'name': 'Prometheus'}]

@app.route('/')
@app.route('/index')
def index():
    # render_template takes the filename as the first argument.
    # Any additional keyword arguments (like 'title' and 'thing') are 
    # passed to the Jinja2 template engine so they can be rendered in the HTML.
    return render_template('index.html',
                           title='My Things',
                           thing=things[0]
                           )
