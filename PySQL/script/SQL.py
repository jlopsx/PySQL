import sqlite3

class DataBase():
    def __init__(self, connection):
        self.connection = sqlite3.connect(connection)

