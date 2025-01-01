import csv
from flask import Flask, jsonify, request
from check_create_schema import check_create_schema
app = Flask(__name__)

schemas = {}  

def check_existance_of_schema(name: str):
    return name in schemas

def create_schema_in_cassandra(data):
    schemas[data["name"]] = data

def update_schema_in_cassandra(name, updated_data):
    schemas[name] = updated_data

def delete_schema_in_cassandra(name):
    if name in schemas:
        del schemas[name]

def get_schema_from_cassandra(name):
    return schemas.get(name, None)


@app.route('/create_schema', methods=['POST'])
def create_schema():
    # Read the JSON from the request body
    data = request.get_json()

    # Check the consistency of the provided JSON
    message, code = check_create_schema(data)

    # If the schema is incorrect -> Send an error to the client
    if code!= 200:
        return message, code
    
    if check_existance_of_schema(data["name"]):
        return jsonify({"message": "Schema already exists"}), 409
    
    create_schema_in_cassandra(data)

    return jsonify({"message": "Schema created successfully"}), 200


@app.route('/schemas/<string:name>', methods=['GET'])
def get_schema(name):
    schema = get_schema_from_cassandra(name)
    if not schema:
        return jsonify({"error": "Schema not found"}), 404
    return jsonify(schema), 200


@app.route('/schemas/<string:name>', methods=['PUT'])
def update_schema(name):
    if not check_existance_of_schema(name):
        return jsonify({"error": "Schema not found"}), 404

    data = request.get_json()
    message, code = check_create_schema(data)
    if code != 200:
        return message, code

    update_schema_in_cassandra(name, data)
    return jsonify({"message": "Schema updated successfully"}), 200


@app.route('/schemas/<string:name>', methods=['PATCH'])
def patch_schema(name):
    if not check_existance_of_schema(name):
        return jsonify({"error": "Schema not found"}), 404

    data = request.get_json()
    existing_schema = get_schema_from_cassandra(name)
    if not existing_schema:
        return jsonify({"error": "Schema not found"}), 404

    for key, value in data.items():
        if key in existing_schema:
            existing_schema[key] = value
    update_schema_in_cassandra(name, existing_schema)
    return jsonify({"message": "Schema patched successfully"}), 200


@app.route('/schemas/<string:name>', methods=['DELETE'])
def delete_schema(name):
    if not check_existance_of_schema(name):
        return jsonify({"error": "Schema not found"}), 404

    delete_schema_in_cassandra(name)
    return jsonify({"message": "Schema deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
