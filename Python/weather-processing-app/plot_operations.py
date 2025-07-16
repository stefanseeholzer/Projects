"""
Description: This class handles the operations to plot data onto a chart.
Author: Stefan Seeholzer, Mitchell Anonsen
Section Number: 251409
Date Created: Mar. 20, 2024
Credit: 
Updates:
"""

import os
import logging
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('WXAgg')

FILE = 'logs.txt'
logging.basicConfig(filename=FILE, level=logging.ERROR)
os.chmod(FILE, 0o666)

class PlotOperations():
    """ Class for plotting weather data onto charts operations. """
    def create_box_plot(self, weather_data, start_year, end_year):
        """ Creates a box plot using specified start and end years. """
        try:
            self.clear_plot()
            years = list(range(start_year, end_year + 1))
            month_temps = {month: [] for month in range(1, 13)}

            for _ in years:
                for month, daily_temps in weather_data.items():
                    month_temps[month].extend(daily_temps)

            month_names = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]

            plt.boxplot([weather_data[month] for month in range(1, 13)])
            plt.xticks(range(1, 13), month_names, rotation=45)
            plt.xlabel("Month")
            plt.ylabel("Temperature in Celcuis")
            plt.title(f"Average Temperatures from {start_year}, {end_year}")
            plt.grid(True)
            plt.show()
        except (ValueError, KeyError, IndexError) as e:
            logging.error("Error creating box plot: %s", e)

    def create_line_plot(self, weather_data, month, year):
        """ Creates a line plot using a specified month and year. """
        try:
            self.clear_plot()
            days = list(range(1, len(weather_data) + 1))

            weather_data_np = np.array(weather_data)
            weather_data_np[weather_data_np is None] = np.nan

            plt.plot(days, weather_data_np, marker='o')
            plt.xticks(range(1, len(weather_data)+1), rotation=45)
            plt.xlabel("Day")
            plt.ylabel("Temperature in Celcuis")
            plt.title(f"Average Daily Temperatures for {month}, {year}")
            plt.grid(True)
            plt.show()
        except (ValueError, KeyError, IndexError) as e:
            logging.error("Error creating line plot: %s", e)

    def clear_plot(self):
        """ Clears the current plot from the screen. """
        plt.clf()

if __name__ == "__main__":
    PlotOperations()
