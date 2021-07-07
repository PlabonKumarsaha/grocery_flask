from datetime import datetime
from sql_connecction import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO gs.orders(order_name,total,datetime) VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid
    # getting the order id and store values in order details using the order_id
    order_details_query = ("INSERT INTO gs.order_details(order_id,product_id, quantity, total_price)"
                           "VALUES (%s, %s , %s, %s);")
    order_details_data = []
    for order_details_record in order['order_details']:
        order_details_data.append([order_id,
                                   int(order_details_record['product_id']),
                                   int(order_details_record['quantity']),
                                   float(order_details_record['total_price']),
                                   ])
    cursor.executemany(order_details_query, order_details_data)
    connection.commit()
    return order_id;

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'Saha ',
        'grand_total':'500',
        'datetime' : datetime.now(),
        'order_details': [
            {
                'product_id': 1,
                'quantity' : 2,
                'total_price':50
            },
            {
                'product_id': 2,
                'quantity': 3,
                'total_price': 150
            },
            {
                'product_id': 5,
                'quantity': 2,
                'total_price': 150
            },

        ]
    }))