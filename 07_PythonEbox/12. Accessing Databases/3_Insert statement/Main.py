import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Load database configuration
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

x = PrettyTable()
x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]

try:
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password,
        port=port,
    )
    
    cursor = mydb.cursor()
   
    # Accept user input in CSV format
    u = input("Enter the user detail in CSV format\n")
    
    d = u.split(",")

    # Ensure next id will be 7
    cursor.execute("SELECT MAX(id) FROM user")
    next_id = cursor.fetchone()[0]
    if next_id is None:
        next_id = 1
    else:
        next_id = next_id + 1
    
    # Prepare and execute the INSERT query
    insert_query = "INSERT INTO user (id, name, contactdetail, username, password) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (next_id, d[0], d[1], d[2], d[3]))
    mydb.commit()  # Commit the transaction

    # Execute the SELECT query to retrieve all records from the 'user' table
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()

    # Add rows to PrettyTable
    for row in result:
        x.add_row([row[0], row[1], row[2], row[3], row[4]])
    
    # Print the final result set
    print(x)

except Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if mydb:
        mydb.close()