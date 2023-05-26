import mysql.connector


class Connection:
    def __init__(self, database='internet_data', host="localhost", user="root", password="password"):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,  # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()


if __name__ == '__main__':
    my_db = Connection()
