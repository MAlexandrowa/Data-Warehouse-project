import csv
from flask import Flask, jsonify, request
from check_create_schema import check_create_schema
app = Flask(__name__)

def check_existance_of_schema(name: str):
    return False

def create_schema_in_cassandra(data):
    pass

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


if __name__ == '__main__':
    app.run(debug=True)
