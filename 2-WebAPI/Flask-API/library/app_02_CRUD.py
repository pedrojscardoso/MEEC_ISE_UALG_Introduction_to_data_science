from flask import Flask, jsonify, abort, request

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


@app.errorhandler(404)
def not_found(error):
    # return an error message and the HTTP status code 404, which HTTP defines as the code for "Not Found".
    # this is a custom error message, called when the requested resource is not found.
    return jsonify({'error': 'Not found'}), 404


@app.route('/iot/api/v1.0/things', methods=['GET'])
def get_things():
    # return the list of things and the HTTP status code 200, which HTTP defines as the code for "OK".
    # 200 is the default status code returned by a server when a request is successful.
    return jsonify(things), 200


@app.route('/iot/api/v1.0/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
    try:
        # return the thing with the given id and the HTTP status code 200, which HTTP defines as the code for "OK".
        return jsonify(things[thing_id]), 200
    except:
        # return an empty JSON object and the HTTP status code 404, which HTTP defines as the code for "Not Found".
        return jsonify({}), 404


@app.route('/iot/api/v1.0/things', methods=['POST'])
def create_thing():
    print(request.json)
    # request.json will have the request data, but only if it came marked as JSON.
    if not request.json \
            or 'name' not in request.json \
            or 'local' not in request.json \
            or 'sensors' not in request.json:
        abort(400)

    global things_counter
    things_counter += 1
    new_thing = {
        'name': request.json['name'],
        'local': request.json['local'],
        'sensors': request.json['sensors']
    }
    things[things_counter] = new_thing

    # return the new thing and the HTTP status code 201, which HTTP defines as the code for "Created".
    # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    return jsonify({things_counter: new_thing}), 201


@app.route('/iot/api/v1.0/things/<int:thing_id>', methods=['PUT'])
def update_thing(thing_id):
    if not request.json:
        abort(400)  # 400 Bad Request

    try:
        thing = things[thing_id]
        thing['name'] = request.json.get('name', thing['name'])
        thing['local'] = request.json.get('local', thing['local'])
        thing['sensors'] = request.json.get('sensors', thing['sensors'])
        # return the updated thing and status code 200, which HTTP defines as the code for "OK
        return jsonify({thing_id: things[thing_id]}), 200
    except:
        abort(404)  # 404 Not Found


@app.route('/iot/api/v1.0/things/<int:thing_id>', methods=['DELETE'])
def delete_thing(thing_id):
    try:
        thing = things[thing_id]
        del things[thing_id]
        # return the deleted thing and status code 200, which HTTP defines as the code for "OK".
        return jsonify({thing_id: thing}), 200
    except:
        abort(404)  # 404 Not Found


if __name__ == '__main__':
    app.run(debug=True)
