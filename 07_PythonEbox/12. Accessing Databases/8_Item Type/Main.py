import mysql.connector,configparser,sys
from mysql.connector import Error
from prettytable import PrettyTable

config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host');
dbname = config.get('DatabaseSection', 'db.schema');
username = config.get('DatabaseSection', 'db.username');
password = config.get('DatabaseSection', 'db.password');
port = config.get('DatabaseSection', 'db.port');

def display_item(cursor):
    cursor.execute("SELECT * FROM item")
    result = cursor.fetchall()
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Deposit", "Cost_per_day"]
    for row in result:
        x.add_row(row)
    print(x)

try:
    connection = mysql.connector.connect(
        host = dburl,
        database = dbname,
        username = username,
        password = password,
        port = port
    )

    cursor = connection.cursor()

    display_item(cursor)

    input_category = input("Enter the category:\n")

    cursor.execute("""
        SELECT c.id, c.name, c.type_id, c.vendor
        FROM category c
        JOIN item i ON c.type_id = i.id
        WHERE i.name = %s
    """, (input_category,))
    
    items = cursor.fetchall()

    if items:
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Type_Id", "Vendor"]
        
        for item in items:
            table.add_row(item)
        
        print(table)
    else:
        print("No such category is present")

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close