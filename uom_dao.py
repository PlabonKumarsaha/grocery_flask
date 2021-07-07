from sql_connecction import get_sql_connection

def get_uoms(connection):
    cursor = connection.cursor()
    query = ("SELECT * frpm gs.uom")
    cursor.execute(query)
    response = []
    for(UOM_ID,UOM_name) in cursor:
        response.append({
            'UOM_ID' : UOM_ID,
            'UOM_name' : UOM_name
        })
    return response;


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_uoms(connection))

