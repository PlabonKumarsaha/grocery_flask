import mysql.connector
from sql_connecction import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT produts.product_id,produts.name,produts.UOM_id, produts.price_per_unit ,uom.UOM_name" \
            " FROM gs.produts inner join gs.uom on produts.UOM_id = uom.UOM_ID;"

    response = []
    cursor.execute(query)

    for (product_id, name, UOM_id, price_per_unit, UOM_name) in cursor:
        # print(product_id, name, UOM_id, price_per_unit, UOM_name)
        response.append({
            'product_id': product_id,
            'name': name,
            'UOM_id': UOM_id,
            'price_per_unit': price_per_unit,
            'UOM_name': UOM_name
        })

    # cnx.close()
    return response;

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO gs.produts(name,UOM_id,price_per_unit)"
             "VALUES(%s,%s,%s)")
    name = product['name'];
    uom = product['UOM_id']
    price = product['price_per_unit']
    cursor.execute(query, (name, uom, price))
    connection.commit()

    return cursor.lastrowid


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO gs.produts(name,UOM_id,price_per_unit)"
             "VALUES(%s,%s,%s)")
    name = product['name'];
    uom = product['UOM_id']
    price = product['price_per_unit']
    cursor.execute(query, (name, uom, price))
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'name': 'Potato',
        'UOM_id': '2',
        'price_per_unit': '12',
    }))
