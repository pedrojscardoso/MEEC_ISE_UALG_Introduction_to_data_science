from flask import Flask, jsonify

app = Flask(__name__)

# list of things... latter you should get this from a database
things = {
    1: {
        'name': 'Prometheus',
        'local': '@lab. 163 / ISE /UAlg',
        'sensors': [
            {'sensor_name': 'mem_sensor', 'units': 'percent'},
            {'sensor_name': 'cpu_sensor', 'units': 'percent'}
        ]
    },
    2: {
        'name': 'Zeus',
        'local': '@lab. 163 / ISE /UAlg',
        'sensors': [
            {'sensor_name': 'temperature', 'units': 'numerical'},
            {'sensor_name': 'humidity', 'units': 'percent'}
        ]
    }
}

things_counter = 2


@app.route('/iot/api/v1.0/things', methods=['GET'])
def get_things():
    return jsonify(things)


@app.route('/iot/api/v1.0/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
    try:
        return jsonify(things[thing_id]), 200
    except:
        return jsonify({}), 404


if __name__ == '__main__':
    app.run(debug=True)
