import mysql.connector

class Connection:

    def create():

        return mysql.connector.connect( 

            host='localhost', 
            port=3306, 
            user='root', 
            password='root', 
            database='db_feedbacks'

        )