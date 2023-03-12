from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index2.html',
                           title='Home',
                           things=things)
