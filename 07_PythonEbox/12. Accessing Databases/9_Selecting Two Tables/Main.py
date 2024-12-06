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

def exhibition_exists(cursor, exhibition_name):
    cursor.execute("SELECT name FROM exhibition WHERE name = %s", (exhibition_name,))
    return cursor.fetchone() is not None

try:
    connection = mysql.connector.connect(
        host = dburl,
        database = dbname,
        username = username,
        password = password,
        port = port
    )
    cursor = connection.cursor()

    exhibition_name = input("Enter the exhibition name:\n").strip()

    while True:
        if exhibition_exists(cursor, exhibition_name):
            break
        else:
            exhibition_name = input("Enter the correct exhibition name:\n").strip()

    cursor.execute("""
            SELECT s.stall_name, s.detail, s.owner_name
            FROM stall s
            JOIN exhibition e ON s.exhibition_id = e.id
            WHERE e.name = %s
        """, (exhibition_name,))

    stalls = cursor.fetchall()
    table = PrettyTable()
    table.field_names = ["Stall Name", "Detail", "Owner Name"]
    for stall in stalls:
        table.add_row(stall)
    print(table)
    
except error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()