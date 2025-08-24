import sqlite3

from src.utils.file import copy_file
from src.config import temp_folder


def interact_database(path : str, database_name : str, requests : str):
    try:
        temp_database = copy_file(path, f"{temp_folder}\\{database_name}")

        connection = sqlite3.connect(temp_database)
        cursor = connection.cursor()

        cursor.execute(requests)
        response = cursor.fetchall()

        cursor.close()
        connection.close()

        return response
    except:
        pass