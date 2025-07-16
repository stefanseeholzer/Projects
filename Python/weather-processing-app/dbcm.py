"""
Description: Database Context Manager.
Author: Stefan Seeholzer, Mitchell Anonsen
Section Number: 251409
Date Created: Mar. 20, 2024
Updates: Apr. 7, 2024
"""

import os
import sqlite3
import logging

FILE = 'logs.txt'
logging.basicConfig(filename=FILE, level=logging.ERROR)
os.chmod(FILE, 0o666)

class DBCM():
    """ This is a context manager to handle connections to a database. """
    def __init__(self, db_name):
        """ Initiates the context manager. """
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        """ Connects to database and returns a cursor. """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, exc_trace):
        """ If no errors, commits changes and closes connection to database. """
        if exc_type is not None:
            self.conn.rollback()
            logging.error("Error: %s: %s", exc_type, exc_value)
        else:
            self.conn.commit()
            self.conn.close()
