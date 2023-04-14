import mysql.connector
from database import cursor
from mysql.connector import errorcode
DB_Name = 'acme'

TABLES = {}
TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`text` varchar(250) NOT NULL,"
    "`user` varchar(250) NOT NULL,"
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB" 
)
def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_Name))
    print("Database {} created!".format(DB_Name))

def create_tables():
    cursor.execute("USE {}".format(DB_Name))
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print('Creating table ({})'.format(table_name),end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)

create_database()
create_tables()