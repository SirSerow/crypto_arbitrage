from asyncio.log import logger
import pymysql
import config
from base_logger import logger

try:
    config = config.get_config('config.ini')
except Exception as ex:
    logger.error(ex)

def connect_db():
    try:
        connection = pymysql.connect(
            host = config.get_setting('config.ini', 'Database', 'host'),
            user = config.get_setting('config.ini', 'Database', 'user_name'),
            password = config.get_setting('config.ini', 'Database', 'password'),
            database = config.get_setting('config.ini', 'Database', 'db_name'),
            cursorclass = pymysql.cursors.DictCursor
        )
    except Exception as ex:
        logger.error("Failed to connect")
        logger.error(ex)