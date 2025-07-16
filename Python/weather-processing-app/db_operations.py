"""
Description: This class handles database operations.
Author: Stefan Seeholzer, Mitchell Anonsen
Section Number: 251409
Date Created: Mar. 20, 2024
Credit: 
Updates:
"""

import os
import logging
import sqlite3
from dbcm import DBCM

FILE = 'logs.txt'
logging.basicConfig(filename=FILE, level=logging.ERROR)
os.chmod(FILE, 0o666)

class DBOperations():
    """ Class for database operations. """
    def initialize_db(self):
        """ Initializes the database and creates a table. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS weather_data
                    (id integer primary key autoincrement,
                    sample_date text,
                    location text,
                    min_temp real,
                    max_temp real,
                    avg_temp real,
                    UNIQUE(sample_date, location));""")
        except sqlite3.Error as e:
            logging.error("Error initializing the database: %s", e)

    def fetch_data(self, sample_date, location):
        """ Fetches data from the database using specified date. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("""SELECT sample_date, location, min_temp, max_temp, avg_temp
                FROM weather_data
                WHERE sample_date = ? AND location = ?""", (sample_date, location))
                return cur.fetchone()
        except sqlite3.Error as e:
            logging.error("Error fetching data from the database: %s", e)
            return None

    def fetch_latest_data(self):
        """ Fetches the last date data was inserted. """
        try:
            with DBCM('weather.sqlite') as cur:
                cur.execute("""SELECT MAX(sample_date)
                FROM weather_data""")
                return cur.fetchone()
        except sqlite3.Error as e:
            logging.error("Error fetching data from the database: %s", e)
            return None

    def fetch_data_by_month(self, start_date, end_date, location):
        """ Fetches data from the database using specified month. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("""SELECT avg_temp
                FROM weather_data
                WHERE sample_date BETWEEN ? AND ?
                AND location = ?""", (start_date, end_date, location))
                return cur.fetchall()
        except sqlite3.Error as e:
            logging.error("Error fetching data from the database: %s", e)
            return None

    def fetch_data_by_year(self, start_date, end_date, location):
        """ Fetches data from the database using specified years. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("""SELECT sample_date, avg_temp
                FROM weather_data
                WHERE sample_date BETWEEN ? AND ?
                AND location = ?""", (start_date, end_date, location))
                return cur.fetchall()
        except sqlite3.Error as e:
            logging.error("Error fetching data from the database: %s", e)
            return None

    def save_data(self, data):
        """ Saves data into the database. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("""INSERT OR IGNORE INTO weather_data
                (sample_date, location, min_temp, max_temp, avg_temp)
                VALUES (?, ?, ?, ?, ?)""", (data['date'], data['location'],
                                            data['Min Temp'], data['Max Temp'],
                                            data['Mean Temp']))
        except sqlite3.Error as e:
            logging.error("Error saving data to the database: %s", e)

    def purge_data(self):
        """ Purges all items in the database. """
        try:
            with DBCM("weather.sqlite") as cur:
                cur.execute("DELETE FROM weather_data")
        except sqlite3.Error as e:
            logging.error("Error removing data from the database: %s", e)

if __name__ == "__main__":
    DBOperations()
