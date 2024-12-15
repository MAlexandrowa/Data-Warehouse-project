from flask import jsonify

def check_create_schema(data):
        # Ensure the data is successfully parsed
    if data is None:
        return jsonify({"error": "JSON is missing"}), 400

    if "name" not in data.keys():
        return jsonify({"error": "Missing 'name' field"}), 400

    if not isinstance(data["name"], str):
        return jsonify({"error": "'name' must be a string"}), 400

    if "columns" not in data.keys():
        return jsonify({"error": "Missing 'columns' field"}), 400

    if not isinstance(data["columns"], list):
        return jsonify({"error": "'columns' must be a list"}), 400

    for column in data["columns"]:
        if "name" not in column.keys():
             return jsonify({"error": "Missing 'name' field in column list"}), 400
        if "@type" not in column.keys():
            return jsonify({"error": "Missing '@type' field in column list"}), 400
        if "is_primary_key" not in column.keys():
            return jsonify({"error": "Missing 'is_primary_key' field in column list"}), 400     
        
    return jsonify({"message": "No issues with schema"}), 200