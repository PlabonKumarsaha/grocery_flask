import mysql.connector
# __cnx means global variable
__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='12345',
                                  host='127.0.0.1',
                                  database='gs')
    return __cnx