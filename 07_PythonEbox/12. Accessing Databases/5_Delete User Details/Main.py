import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Read database configuration from a properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
dbuser = config.get('DatabaseSection', 'db.username')
dbpassword = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

# Initialize the PrettyTable with headers
x = PrettyTable()
x.field_names = ["ID", "Name", "Mobile", "Username", "Password"]

try:
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=dbuser,
        password=dbpassword,
        port=port
    )

    cursor = connection.cursor()

    # Fetch and display all users initially
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()

    for row in result:
        x.add_row(row)

    print(x)

    # Prompt the user to enter the username to be deleted
    username_to_delete = input("Enter the username to be deleted:\n")
    
    # Check if the user exists
    cursor.execute("SELECT * FROM user WHERE username = %s", (username_to_delete,))
    user_to_delete = cursor.fetchone()

    if user_to_delete:
        # Delete the user if found
        cursor.execute("DELETE FROM user WHERE username = %s", (username_to_delete,))
        connection.commit()
        print(f"Username {username_to_delete} with id={user_to_delete[0]} deleted successfully")

        # Display the updated user table
        cursor.execute("SELECT * FROM user")
        updated_users = cursor.fetchall()
        x.clear_rows()
        for user in updated_users:
            x.add_row(user)
        print(x)
    else:
        print("User not found")
        print(x)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
