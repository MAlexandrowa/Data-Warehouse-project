import csv
from flask import Flask, jsonify

app = Flask(__name__)

# Функция за четене на CSV файл и връщане на данни като списък от речници
def read_csv(file_name):
    data = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data

# Endpoint за зареждане на данни от 'account.asc'
@app.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = read_csv('account.asc')
    return jsonify(accounts)

# Endpoint за зареждане на данни от 'card.asc'
@app.route('/cards', methods=['GET'])
def get_cards():
    cards = read_csv('card.asc')
    return jsonify(cards)

# Endpoint за зареждане на данни от 'client.asc'
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = read_csv('client.asc')
    return jsonify(clients)

# Endpoint за зареждане на данни от 'disp.asc'
@app.route('/disp', methods=['GET'])
def get_disp():
    disp = read_csv('disp.asc')
    return jsonify(disp)

# Endpoint за зареждане на данни от 'district.asc'
@app.route('/districts', methods=['GET'])
def get_districts():
    districts = read_csv('district.asc')
    return jsonify(districts)

# Endpoint за зареждане на данни от 'loan.asc'
@app.route('/loans', methods=['GET'])
def get_loans():
    loans = read_csv('loan.asc')
    return jsonify(loans)

# Endpoint за зареждане на данни от 'order.asc'
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = read_csv('order.asc')
    return jsonify(orders)

# Endpoint за зареждане на данни от 'trans.asc'
@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = read_csv('trans.asc')
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
