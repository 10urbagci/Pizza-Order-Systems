from flask import Flask, render_template
import psycopg2
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

app = Flask(__name__)

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Ana sayfa
@app.route("/")
def index():
    # Fetch data from database
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders_database")
    rows = cur.fetchall()

    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run()