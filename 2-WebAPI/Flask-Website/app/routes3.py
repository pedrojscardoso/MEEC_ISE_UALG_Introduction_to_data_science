from flask import render_template
from app import app


things = [{'id': 1, 'name': 'Prometheus'}]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='My Things',
                           thing=things[0]
                           )
