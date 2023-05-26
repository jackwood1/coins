import mysql.connector


class Connection:
    def __init__(self, database='coin_db', host="127.0.0.1", user="root", password="password"):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,  # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

