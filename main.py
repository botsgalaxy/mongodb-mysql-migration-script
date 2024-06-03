import pymongo
import mysql.connector
from mysql.connector import errorcode
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__file__)

mongo_db_name = 'test_database'
mongo_collection_name = 'test_collection'

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = ''
mysql_db_name = 'test_database'

logger.info("Connecting to MongoDB")
mongo_client = pymongo.MongoClient("mongodb://root:password@localhost:27017")
mongo_db = mongo_client[mongo_db_name]
mongo_collection = mongo_db[mongo_collection_name]

logger.info("Getting data from MongoDB")
mongo_data = mongo_collection.find()

try:
    logger.info("Connecting to MySQL")
    mysql_conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db_name
    )
    mysql_cursor = mysql_conn.cursor()

    insert_query = """
    INSERT INTO test_table (id, first_name, last_name, balance)
    VALUES (%s, %s, %s, %s)
    """
    
    for document in mongo_data:
        field1 = document.get('id')
        field2 = document.get('first_name')
        field3 = document.get('last_name')
        field4 = document.get('balance')
        
        logger.info(f"Executing query for document id {field1}")
        mysql_cursor.execute(insert_query, (field1, field2, field3, field4))
    
    logger.info("Committing changes to MySQL")
    mysql_conn.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        logger.error("Access denied: check your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logger.error("Database does not exist")
    else:
        logger.error(err)
finally:
    if mysql_conn.is_connected():
        logger.info("Closing MySQL connection")
        mysql_cursor.close()
        mysql_conn.close()

logger.info("Closing MongoDB connection")
mongo_client.close()
