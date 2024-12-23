from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'GET login'
    elif request.method == 'POST':
        return 'POST login'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return 'GET register'
    elif request.method == 'POST':
        return 'POST register'

@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        return 'GET logout'
    elif request.method == 'POST':
        return 'POST logout'
    elif request.method == 'DELETE':
        return 'DELETE logout'

@app.route('/profile', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def profile():
    if request.method == 'GET':
        return 'GET profile'
    elif request.method in ['PUT', 'PATCH']:
        return 'UPDATE profile'
    elif request.method == 'DELETE':
        return 'DELETE profile'

@app.route('/profile/favourites', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def favourites():
    if request.method == 'GET':
        return 'GET favourites'
    elif request.method == 'POST':
        return 'POST favourites'
    elif request.method == 'DELETE':
        return 'DELETE favourites'
    elif request.method == 'PATCH':
        return 'PATCH favourites'

@app.route('/profile/favourites/<favourite_id>', methods=['DELETE'])
def favourite_detail(favourite_id):
    return f'DELETE favourite {favourite_id}'

@app.route('/profile/search_history', methods=['GET', 'DELETE'])
def search_history():
    if request.method == 'GET':
        return 'GET search history'
    elif request.method == 'DELETE':
        return 'DELETE search history'

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return 'GET items'
    elif request.method == 'POST':
        return 'POST items'

@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        return f'GET item {item_id}'
    elif request.method == 'DELETE':
        return f'DELETE item {item_id}'

@app.route('/leasers', methods=['GET'])
def leasers():
    return 'GET leasers'

@app.route('/leasers/<leaser_id>', methods=['GET'])
def leaser_detail(leaser_id):
    return f'GET leaser {leaser_id}'

@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        return 'GET contracts'
    elif request.method == 'POST':
        return 'POST contracts'

@app.route('/contracts/<contract_id>', methods=['GET', 'PATCH', 'PUT'])
def contract_detail(contract_id):
    if request.method == 'GET':
        return f'GET contract {contract_id}'
    elif request.method in ['PATCH', 'PUT']:
        return f'UPDATE contract {contract_id}'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'GET search'
    elif request.method == 'POST':
        return 'POST search'

@app.route('/complain', methods=['POST'])
def complain():
    return 'POST complain'

@app.route('/compare', methods=['GET', 'PUT', 'PATCH'])
def compare():
    if request.method == 'GET':
        return 'GET compare'
    elif request.method in ['PUT', 'PATCH']:
        return 'UPDATE compare'

if __name__ == '__main__':
    app.run()
