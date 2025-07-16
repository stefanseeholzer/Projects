"""
Description: Environment Canada WebScraper
Author:Mitchell Anonsen & Stefan Seeholzer
Section Number:251409
Date Created:March 19th,2024
Credit: 
Updates:
"""

import os
import logging
from html.parser import HTMLParser
from datetime import datetime

FILE = 'logs.txt'
logging.basicConfig(filename=FILE, level=logging.ERROR)
os.chmod(FILE, 0o666)

class WeatherScraper(HTMLParser):
    """Class for scraping weather data from Environment Canada"""
    def __init__(self):
        """Creates a modified HTMLParser with needed variables"""
        super().__init__()
        self.inside_table = False
        self.inside_tbody = False
        self.inside_row = False
        self.inside_cell = False
        self.inside_abbr = False
        self.inside_a = False
        self.still_data = True
        self.column_index = 0
        self.data = {}
        self.date =datetime
        self.daily_temps = {}
        self.weather = {}
        self.row_count = 0


    def handle_starttag(self, tag, attrs):
        """Finds the proper starting tags on page(s) to handle searching for data"""
        if tag == 'table':
            self.inside_table = True
        elif self.inside_table:
            if tag == 'tbody':
                self.inside_tbody = True
            elif tag == 'tr':
                self.inside_row = True
                self.column_index = 0
            elif tag == 'td':
                self.inside_cell = True
            elif tag == 'th':
                for attr in attrs:
                    if attr[0] == 'scope' and attr[1] == 'row':
                        self.inside_cell = True
                        break
            elif tag == 'abbr' and self.inside_tbody:
                for attr in attrs:
                    if attr[0] == 'title':
                        if attr[1] == 'Average' or attr[1] == 'Extreme':
                            return
                        else:
                            self.inside_abbr = True
                            date_string = attr[1]
                            date_format = "%B %d, %Y"
                            try:
                                parsed_date = datetime.strptime(date_string, date_format)
                                self.date = parsed_date.strftime("%Y-%m-%d")
                                self.data[self.date] = {}
                            except ValueError as e:
                                logging.error("Error parsing date string '%s' for date: %s", date_string, e)
        elif tag == 'a':
            self.inside_a = True

    def handle_endtag(self, tag):
        """Finds the proper ending tags on page(s) to handle searching for data"""
        if tag == 'table':
            self.inside_table = False
        elif tag == 'tbody':
            self.inside_tbody = False
        elif tag == 'tr':
            self.inside_row = False
        elif tag in ('td', 'th'):
            self.inside_cell = False
        elif tag == 'abbr':
            self.inside_abbr = False
            self.column_index = 0
        elif tag == 'a':
            self.inside_a = False



    def handle_data(self, data):
        """Grabs the data in relevant tags and stores them in dictionaries"""
        if (self.inside_table and self.inside_row and self.inside_cell and
            self.still_data and not self.inside_a):
            data = data.strip()
            if '<' in data:
                data = ''
            if self.column_index == 0 and 'Sum' in data:
                self.still_data = False
            if self.column_index <= 3:
                if self.date in self.data:
                    if self.column_index == 1:
                        try:
                            self.data[self.date]['Max Temp'] = data
                        except ValueError:
                            logging.error("Error converting Max Temp to float: %s: %s: %s",
                                          ValueError, self.date, data)
                    elif self.column_index == 2:
                        try:
                            self.data[self.date]['Min Temp'] = data
                        except ValueError:
                            logging.error("Error converting Min Temp to float: %s: %s: %s",
                                          ValueError, self.date, data)
                    elif self.column_index == 3:
                        try:
                            self.data[self.date]['Mean Temp'] = data
                        except ValueError:
                            logging.error("Error converting Mean Temp to float: %s: %s: %s",
                                          ValueError, self.date, data)
            self.column_index += 1


if __name__ == "__main__":
    WeatherScraper()
