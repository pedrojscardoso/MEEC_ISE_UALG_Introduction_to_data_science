"""
Example 5: Advanced Template Rendering
This script is nearly identical to routes4.py, but it demonstrates 
that by simply hitting a different template file ('index3.html'), 
we can completely change the presentation of the same data using 
features like Template Inheritance (e.g., {% extends "base.html" %}).
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Mock data representing multiple IoT things
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
    
    # Rendering index3.html which likely extends a base layout
    return render_template('index3.html', title='Sensors Home!', things=things)
