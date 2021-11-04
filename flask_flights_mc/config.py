import os
# CONFIG OBJECT FOR CALLING MY .ENV FILE WITH MY ENVIRONEMNT VARIABLES AND USING WHAT EVER THOSE VARIABLES MAY BE. MORE SECURE. MORE DYNAMIC.
config = {
    'host': os.environ.get('MYSQL_HOST'),
    'port': os.environ.get('MYSQL_PORT'),
    'user': os.environ.get('MYSQL_USER'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'database': os.environ.get('MYSQL_DB'),
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
# specify connection string
DATABASE_CONNECTION_URI = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
