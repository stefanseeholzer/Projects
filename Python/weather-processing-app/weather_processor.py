"""
Description: This class handles the processing of data with user interaction.
Author: Stefan Seeholzer, Mitchell Anonsen
Section Number: 251409
Date Created: Mar. 20, 2024
Credit: 
Updates:
"""

# pylint weather_processor.py --extension-pkg-whitelist=wx

import os
import logging
import threading
import urllib.request
from datetime import datetime, timedelta
import numbers
import wx
from db_operations import DBOperations
from plot_operations import PlotOperations
from scrape_weather import WeatherScraper

FILE = 'logs.txt'
logging.basicConfig(filename=FILE, level=logging.ERROR)
os.chmod(FILE, 0o666)

class WeatherProcessor(wx.Frame):
    """ Class to download and view weather data. """
    def __init__(self, parent, title):
        """ Initialises the Weather Processor and sets variables and initiate user interface. """
        super().__init__(parent, title=title, size=(800, 600))
        self.db_ops = DBOperations()
        self.plot_ops = PlotOperations()
        self.init_ui()

    def init_ui(self):
        """ Method to set user interface for the program. """
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Lineplot box
        lineplot_static_box = wx.StaticBox(panel, wx.ID_ANY, "Line Plot")
        lineplot_static_box.SetBackgroundColour(wx.Colour(192,192,192))
        vbox_lineplot = wx.StaticBoxSizer(lineplot_static_box, wx.VERTICAL)
        hbox_lineplot = wx.BoxSizer(wx.HORIZONTAL)

        months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

        # Boxplot box
        boxplot_static_box = wx.StaticBox(panel, wx.ID_ANY, "Box Plot")
        boxplot_static_box.SetBackgroundColour(wx.Colour(192,192,192))
        vbox_boxplot = wx.StaticBoxSizer(boxplot_static_box, wx.VERTICAL)
        hbox_boxplot = wx.BoxSizer(wx.HORIZONTAL)

        # Download button
        download_data_btn = wx.Button(panel, label="Download Weather Data")
        download_data_btn.Bind(wx.EVT_BUTTON, self.on_download_data)
        vbox.Add(download_data_btn, 0, wx.ALL | wx.EXPAND, 10)

        # Update button
        update_data_btn = wx.Button(panel, label="Update Weather Data")
        update_data_btn.Bind(wx.EVT_BUTTON, self.on_update_data)
        vbox.Add(update_data_btn, 0, wx.ALL | wx.EXPAND, 10)

        # Boxplot
        start_year_label = wx.StaticText(panel, label="Enter Start Year:")
        hbox_boxplot.Add(start_year_label, 0, wx.ALL | wx.EXPAND, 10)
        self.start_year_input = wx.TextCtrl(panel, size=(200, -1))
        hbox_boxplot.Add(self.start_year_input, 0, wx.ALL | wx.EXPAND, 10)

        end_year_label = wx.StaticText(panel, label="Enter End Year:")
        hbox_boxplot.Add(end_year_label, 0, wx.ALL | wx.EXPAND, 10)
        self.end_year_input = wx.TextCtrl(panel, size=(200, -1))
        hbox_boxplot.Add(self.end_year_input, 0, wx.ALL | wx.EXPAND, 10)

        boxplot_btn = wx.Button(panel, label="Create Box Plot")
        boxplot_btn.Bind(wx.EVT_BUTTON, self.on_create_box_plot)
        vbox_boxplot.Add(hbox_boxplot, 0, wx.ALL | wx.EXPAND, 10)
        vbox_boxplot.Add(boxplot_btn, 0, wx.ALL | wx.EXPAND, 10)
        vbox.Add(vbox_boxplot, 0, wx.ALL | wx.EXPAND, 10)

        # Lineplot
        month_label = wx.StaticText(panel, label="Enter Month:")
        hbox_lineplot.Add(month_label, 0, wx.ALL | wx.EXPAND, 10)
        self.month_input = wx.Choice(panel, choices = months)
        hbox_lineplot.Add(self.month_input, 0, wx.ALL | wx.EXPAND, 10)

        year_label = wx.StaticText(panel, label="Enter Year:")
        hbox_lineplot.Add(year_label, 0, wx.ALL | wx.EXPAND, 10)
        self.year_input = wx.TextCtrl(panel, size=(200, -1))
        hbox_lineplot.Add(self.year_input, 0, wx.ALL | wx.EXPAND, 10)

        lineplot_btn = wx.Button(panel, label="Create Line Plot")
        lineplot_btn.Bind(wx.EVT_BUTTON, self.on_create_line_plot)
        vbox_lineplot.Add(hbox_lineplot, 0, wx.ALL | wx.EXPAND, 10)
        vbox_lineplot.Add(lineplot_btn, 0, wx.ALL | wx.EXPAND, 10)
        vbox.Add(vbox_lineplot, 0, wx.ALL | wx.EXPAND, 10)

        # finish up
        panel.SetSizer(vbox)
        self.Center()
        self.Show()

    def on_download_data(self, event):
        """
            Method that downloads all weather data from the web
            and adds it to the database.
        """
        def download_data_thread():
            try:
                self.db_ops.purge_data()
            except Exception as e:
                logging.info("Error purging data:", e)
                #Log the error and then exit the function to prevent further execution
                return
            try:
                self.db_ops.initialize_db()
            except Exception as e:
                logging.info("Error initializing database:", e)
                #Log the error and then exit the function to prevent further execution
                return

            logging.info("Downloading weather data...")
            print("Downloading weather data...")

            base_url = ('https://climate.weather.gc.ca'
                        '/climate_data/daily_data_e.html'
                        '?StationID=27174&timeframe=2')
            current_date = datetime.now().replace(day=1)
            while True:
                current_month_url = (f"{base_url}&StartYear={current_date.year}"
                                    f"&EndYear={current_date.year}&Day=1"
                                    f"&Year={current_date.year}&Month={current_date.month}")
                try:
                    with urllib.request.urlopen(current_month_url) as response:
                        html = str(response.read(), 'utf-8')  # Decode bytes to string
                    myscraper = WeatherScraper()
                    myscraper.feed(html)  # Feed the HTML content to the parser
                    data = myscraper.data
                    if current_date.month == 1:
                        current_date = current_date.replace(year=current_date.year - 1, month=12)
                    else:
                        current_date = current_date.replace(month=current_date.month - 1)
                    if not data:
                        break
                    else:
                        for date, temps in data.items():
                            weather_info = {
                                'date': date,
                                'location': "Winnipeg",
                                'Min Temp': temps['Min Temp'],
                                'Max Temp': temps['Max Temp'],
                                'Mean Temp': temps['Mean Temp']
                            }
                            self.db_ops.save_data(weather_info)
                except Exception as e:
                    logging.error(f"Error downloading weather data: {e}")

            logging.info("Data successfully inserted into database.")
            print("Data successfully inserted into database.")

        download_thread = threading.Thread(target=download_data_thread)
        download_thread.start()

    def on_update_data(self, event):
        """
            Method that updates the data in the database with all current
            weather data from the web.
        """

        logging.info("Updating weather data...")
        print("Updating weather data...")

        self.db_ops.initialize_db()
        latest_data = self.db_ops.fetch_latest_data()

        base_url = ('https://climate.weather.gc.ca/climate_data/'
                    'daily_data_e.html?StationID=27174&timeframe=2')
        current_date = datetime.now().replace(day=1)
        found_latest = False
        while True:
            current_month_url = (f"{base_url}&StartYear={current_date.year}"
                                 f"&EndYear={current_date.year}&Day=1"
                                 f"&Year={current_date.year}&Month={current_date.month}")
            with urllib.request.urlopen(current_month_url) as response:
                html = str(response.read(), 'utf-8')  # Decode bytes to string
            myscraper = WeatherScraper()
            myscraper.feed(html)  # Feed the HTML content to the parser
            data = myscraper.data
            if current_date.month == 1:
                current_date = current_date.replace(year=current_date.year - 1, month=12)
            else:
                current_date = current_date.replace(month=current_date.month - 1)
            if not data:
                break
            else:
                for date, temps in data.items():
                    if date == latest_data[0]:
                        found_latest = True
                        break
                    weather_info = {
                        'date': date,
                        'location': "Winnipeg",
                        'Min Temp': temps['Min Temp'],
                        'Max Temp': temps['Max Temp'],
                        'Mean Temp': temps['Mean Temp']
                    }
                    self.db_ops.save_data(weather_info)
            if found_latest:
                break

        print("Successfully updated weather data.")

    def on_create_box_plot(self, event):
        """ Method that creates a box plot using the user's selected years. """
        print("Creating box plot for selected years...")

        try:
            start_year = int(self.start_year_input.GetValue())
            end_year = int(self.end_year_input.GetValue())
            start_date = datetime(int(start_year), 1, 1)
            end_date = datetime(int(end_year), 12, 31)
            start_date = start_date - timedelta(days=1)
            weather_data = {}

            data = self.db_ops.fetch_data_by_year(start_date, end_date, "Winnipeg")
            if not data:
                raise ValueError("No data for these years.")

            for date, temp in data:
                date_time = datetime.strptime(date, '%Y-%m-%d')
                month = date_time.month

                if isinstance(temp, numbers.Number):
                    if month in weather_data:
                        weather_data[month].append(temp)
                    else:
                        weather_data[month] = [temp]
            self.plot_ops.create_box_plot(weather_data, start_year, end_year)
            print("Successfully created box plot for selected years.")
        except ValueError as ve:
            wx.MessageBox(str(ve), "Error", wx.OK | wx.ICON_ERROR)

    def on_create_line_plot(self, event):
        """ Method that creates a line plot using the user's selected month. """
        print("Creating line plot for selected month...")

        try:
            selected_month = self.month_input.GetSelection()+1
            month_name = self.month_input.GetStringSelection()
            selected_year = int(self.year_input.GetValue())
            start_date = datetime(selected_year, selected_month, 1)
            end_date = start_date.replace(day=28) + timedelta(days=4)
            end_date = end_date - timedelta(days=end_date.day)
            start_date = start_date - timedelta(days=1)

            data = self.db_ops.fetch_data_by_month(start_date, end_date, "Winnipeg")

            if len(data) == 0:
                raise ValueError("No data for this month.")

            formatted_data = [item[0] if isinstance(item[0], numbers.Number) else None for item in data]

            self.plot_ops.create_line_plot(formatted_data, month_name, selected_year)
            print("Successfully created a line plot for the selected month.")
        except ValueError as ve:
            wx.MessageBox(str(ve), "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App()
    frame = WeatherProcessor(None, title = "Weather Processing App")
    frame.Show()
    app.MainLoop()
