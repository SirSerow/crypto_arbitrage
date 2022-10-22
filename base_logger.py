'''
Module for handling logs
'''

from fileinput import filename
import logging

from logging.handlers import RotatingFileHandler


file_name = 'arbitrage.log'

logger = logging
'''
Initialise logger 
'''

logger.basicConfig( level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                    handlers = [RotatingFileHandler(file_name, maxBytes=2000000, backupCount=10)])
