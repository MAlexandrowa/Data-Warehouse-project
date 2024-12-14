import csv
from flask import Flask, jsonify

app = Flask(__name__)

def read_csv(file_name):
    data = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = read_csv('account.asc')
    return jsonify(accounts)

@app.route('/cards', methods=['GET'])
def get_cards():
    cards = read_csv('card.asc')
    return jsonify(cards)

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = read_csv('client.asc')
    return jsonify(clients)

@app.route('/disp', methods=['GET'])
def get_disp():
    disp = read_csv('disp.asc')
    return jsonify(disp)

@app.route('/districts', methods=['GET'])
def get_districts():
    districts = read_csv('district.asc')
    return jsonify(districts)

@app.route('/loans', methods=['GET'])
def get_loans():
    loans = read_csv('loan.asc')
    return jsonify(loans)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = read_csv('order.asc')
    return jsonify(orders)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = read_csv('trans.asc')
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
