import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import re


class MysqlDb:

    def search(self, data, table_name='gene_autocomplete'):
        load_dotenv('.env')
        try:
            connection = mysql.connector.connect(host=os.getenv("DB_HOST"),
                                                 database=os.getenv("DB_NAME"),
                                                 user=os.getenv("DB_USERNAME"),
                                                 password=os.getenv("DB_PASSWORD"))
            cursor = connection.cursor(buffered=True)

            # check if exist
            if data['species']:
                cursor.execute(
                    "SELECT stable_id as id,display_label as name,species FROM " + table_name + " WHERE display_label LIKE"
                                                                                                " '"+data['name']+"%'"
                                                                                               "AND species = %s",
                    (data['species'],)
                )
            else:
                cursor.execute(
                    "SELECT stable_id as id,display_label as name,species FROM " + table_name + " WHERE display_label LIKE '"
                                                                                                ""+data['name']+"%'"

                )
            # gets the number of rows affected by the command executed
            row_data = cursor.fetchall()

            cursor.close()
            return row_data
        except Error as e:
            print("Error while connecting to MySQL: ", e)
            return False
