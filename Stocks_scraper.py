import requests
from datetime import datetime
import math
from Logger import logger_app
from DB import Database_Operations

class StockInfo:

    Base_url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true'
    def __init__(self,start_year,end_year):
        self.logger = logger_app
        self.start_period = start_year
        self.end_period = end_year
    def Date(self):
        self.logger('Entered the Date object of the Stockinfo class').Logger()
        '''The Date function take input for the years month and day and the format should be yyyy,mm,dd'''

        try:

            Start_period = [int(self.start_period[0]),int(self.start_period[1]),int(self.start_period[2])]
            End_period = [int(self.end_period[0]),int(self.end_period[1]),int(self.end_period[2])]
            self.logger('The start dates and end dates are imputed sucesfully').Logger()
        except Exception as e:
              print(e)
        else:
              return (Start_period,End_period)

    def TimeStamp(self):

        self.logger('Entered the timestamp object of the Stockinfo class ').Logger()
        '''Start_date is the record from where you want to start
        End date is the record where you want to end
        Both the parameter must take list formats
        eg:start_Period=[yy,mm,dd],End_Preiod=[yy,mm,dd]'''

        try:
            Start_Period,End_Period = self.Date()
            Period1 = datetime(year=Start_Period[0],month=Start_Period[1],day=Start_Period[2])
            Period2 = datetime(year=End_Period[0],month=End_Period[1],day=End_Period[2])
            self.logger('Time Stamp calculated sucesfully').Logger()
        except Exception as e:
            self.logger('Enter the dates Properly').Logger()
        else:
            Time_stamp_start=datetime.timestamp(Period1)
            Time_stamp_End=datetime.timestamp(Period2)
            period=(math.trunc(Time_stamp_start),math.trunc(Time_stamp_End))
            return period

    def Stock_data(self,stock_name):
      self.logger('Entered the Stock_data object of the stockinfo class').Logger()
      '''This will establish the connection between the website and the user'''
      try:
          agent1 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
          headers1 = {'User-Agent': agent1}
          Stock_name=stock_name
          periods=self.TimeStamp()
          response=requests.get(self.Base_url.format(stock_name,periods[0],periods[1]),headers=headers1)
      except Exception as e:
        self.logger('Something wrong'),print(e)
      else:
          with open(stock_name+'.csv','wb') as f:
              f.write(response.content)
          Database_Operations(database_name='financialdata', Table_name=Stock_name.split('.')[0],file_name=Stock_name+'.csv').create_databases()