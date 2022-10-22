'''
Module for handling config files
'''
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os


def create_config(path):  
    '''
    Create config file
    '''
    config = configparser.ConfigParser() 
    config.add_section("Database")
    config.set("Database", "password", "your_password")
    config.set("Database", "user_name", "your_user")
    config.set("Database", "host", "localhost")
    config.set("Database", "db_name", "arbitrage_bd")

    with open(path, 'w') as config_file:
        config.write(config_file)


def get_config(path):
    '''
    Returns config object
    '''
    if not os.path.exists(path):
        create_config()
    
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    '''
    Return config value
    '''
    config = get_config(path)
    value = config.get(section, setting)
    return value

def update_setting(path, section, setting, value):
    '''
    Update setting
    '''
    config = get_config(path)
    config.set(section, setting, value)
    with open(path) as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "config.ini"
    create_config(path)
