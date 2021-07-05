import mysql.connector


def get_all_products():
    cnx = mysql.connector.connect(user='root', password='12345',
                                  host='127.0.0.1',
                                  database='gs')
    cursor = cnx.cursor()
    query = "SELECT produts.product_id,produts.name,produts.UOM_id, produts.price_per_unit ,uom.UOM_name" \
            " FROM gs.produts inner join gs.uom on produts.UOM_id = uom.UOM_ID;"

    response = []
    cursor.execute(query)

    for (product_id, name, UOM_id, price_per_unit, UOM_name) in cursor:
        #print(product_id, name, UOM_id, price_per_unit, UOM_name)
        response.append({
            'product_id' :product_id,
            'name' : name,
            'UOM_id':UOM_id,
            'price_per_unit':price_per_unit,
            'UOM_name':UOM_name
        })

    cnx.close()
    return response;

if __name__ == '__main__':
    print(get_all_products())
