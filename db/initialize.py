import mysql.connector
import os

class DBManager:
    def __init__(self, database='coin_db', host="localhost", user="root", password="password"):
        #TODO this will fail if the db does not exist
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,  # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def execute_scripts_from_file(self, filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        #TODO fix this, creates empty query
        sql_commands = sqlFile.split(';')

        for command in sql_commands:
            try:
                self.cursor.execute(command)
                print(command)
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

    def load_schema_files(self):
        path = './schema/'
        files = os.listdir(path)
        for file in files:
            self.execute_scripts_from_file(path + file)


    def load_data_files(self):
        path = './data/'
        files = os.listdir(path)
        for file in files:
            self.execute_scripts_from_file(path + file)


    def create_db(self):
        self.cursor.execute('CREATE DATABASE coin_db')
        self.cursor.execute("SHOW DATABASES")
        for x in self.cursor:
            print(x)


    def drop_db(self):
        self.cursor.execute('DROP DATABASE coin_db')
        self.cursor.execute("SHOW DATABASES")
        for x in self.cursor:
            print(x)



if __name__ == '__main__':
    my_db = DBManager();
    #my_db.create_db()
    my_db.load_schema_files()
    my_db.load_data_files()
