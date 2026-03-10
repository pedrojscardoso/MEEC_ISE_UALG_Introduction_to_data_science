"""
Example 4: Passing Lists to Templates
Here we pass a list of dictionaries to the template.
This allows the Jinja2 template (index2.html) to use a 'for' loop 
to generate HTML dynamically for every item in the list.
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Mock data representing multiple IoT things, each with multiple sensors
    things = [
        {
            'id': 1,
            'name': 'Prometheus',
            'local': '@lab. 163 / ISE /UAlg',
            'sensors': [
                {'sensor_name': 'mem_sensor', 'units': 'percent'},
                {'sensor_name': 'cpu_sensor', 'units': 'percent'}
            ]
        },
        {
            'id': 2,
            'name': 'Zeus',
            'local': '@lab. 163 / ISE /UAlg',
            'sensors': [
                {'sensor_name': 'temperature', 'units': 'numerical'},
                {'sensor_name': 'humidity', 'units': 'percent'}
            ]
        }
    ]
    
    # We pass the entire 'things' list to the template
    return render_template('index2.html',
                           title='Home',
                           things=things)
