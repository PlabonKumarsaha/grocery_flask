from flask import Flask, request, jsonify
import products_dao
from sql_connecction import get_sql_connection

app = Flask(__name__)
connection = get_sql_connection()


@app.route('/hello')
def hello():
    return "hello!how"


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    retrun_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : retrun_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    print("starting python flask sever")
    app.run(port=5000)
