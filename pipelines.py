# Import Libraries
import requests
import psycopg2
import configparser
from binance import Client

# Read configuration from the INI file
config = configparser.ConfigParser()
config.read('config.ini')

# Binance API credentials
API_KEY = config.get('binance', 'api_key')
API_SECRET = config.get('binance', 'api_secret')

# PostgreSQL database connection
DB_NAME = config.get('postgres', 'db_name')
DB_USER = config.get('postgres', 'db_user')
DB_PASSWORD = config.get('postgres', 'db_password')
DB_HOST = config.get('postgres', 'db_host')
DB_PORT = config.get('postgres', 'db_port')

# Connect to the PostgreSQL database

# Create a connection
conn = psycopg2.connect(
    dbname = DB_NAME,
    user = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST,
    port = DB_PORT
)

# Create a cursor
cur = conn.cursor()

client = Client(API_KEY, API_SECRET)

prices = client.get_all_tickers()