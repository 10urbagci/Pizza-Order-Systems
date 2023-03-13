import psycopg2
import pandas as pd
import configparser


# Load configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')


# Get database configuration parameters
host = config['Pizza']['host']
database = config['Pizza']['database']
user = config['Pizza']['user']
password = config['Pizza']['password']
port = config['Pizza']['port']


conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Create a cursor object
cur = conn.cursor()

"""
# Create table in the database
create_table = '''CREATE TABLE orders_database (
    pizza_type TEXT,
    name TEXT,
    id_card_no BIGINT,
    card_number BIGINT,
    exp_date TEXT,
    cvv INTEGER,
    description TEXT,
    sauce_description TEXT,
    order_date DATE,
    total_price INTEGER

);'''

cur.execute(create_table)
conn.commit()
"""

# Create a cursor object
cur = conn.cursor()

df = pd.read_csv('Orders_Database.csv')

# Insert data into the database
for index, row in df.iterrows():
    cur.execute("INSERT INTO orders_database (pizza_type, name, id_card_no, card_number, exp_date, cvv, description, sauce_description, order_date, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        row['pizza_type'],
        row['name'],
        row['id_card_no'],
        row['card_number'],
        row['exp_date'],
        row['cvv'],
        row['description'],
        row['sauce_description'],
        row['order_date'],
        row['total_price']
    ))

conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
