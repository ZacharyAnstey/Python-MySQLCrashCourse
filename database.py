import mysql.connector


config = {
    'user': 'root',
    'password': 'Skip1234.',
    'host': 'localhost',
    'database': 'acme'
}
db = mysql.connector.connect(**config)
cursor = db.cursor()