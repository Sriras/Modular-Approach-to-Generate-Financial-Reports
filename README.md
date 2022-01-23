# Modular approach to gernerate financial reports

## Introduction to Stock Market
In a country like ours where free market economy is the life line, Stock Market is one of the primary source for higher Capital for any business venture and development. This is the place where there is no disparity, in the participants, democratized access to trading and exchange of 
capital for Investors Big and Small. Stock Market is a market place where buyers and sellers participate to trade the shares of public corporations. A licensed gambling den. An individual purchasing shares is called the buyer of shares and one who sells the shares is the seller. Here both purchasers and sellers can be an Individuals or a Companies (Mutual funds, LIC, 
Pensioners Fund). What is a public company or corporation? Their shares are freely tradable in the stock market. These companies get themselves registered in the stock exchange, for the purpose of getting capital for starting business or expanding it.

Share and Stocks: Shares are a unit of ownership in a company of any individual that could be held and sold. Stocks are cumulative form of shares, usually held and sold together. A company in need of capital approaches the share market and sell the company’s share for a price 
determined by the market. Usually each share price is fixed at Rs.2, Rs.5 or Rs.10. The company is free to sell those shares in the market either at the fixed price or at a premium over the fixed price depending on market tendencies for that company. Shares are held by 
employees, the public and the promoters of the company. The shares of the company once sold in the market, realizes the capital for the company and it is done. Now the holders of the shares of the company, reap the benefits for their investments depending on how the company 
performs and the declared dividend of the company.

## Required libraries
- Flask 
- request,render_template,send_file
- os
- shutil
- docx
- mysql.connector
- datetime
- math
- pandas
- numpy
- scipy
- keras.models
- keras.layers
- sklearn
- matplotlib 
- statsmodel

## Dataset Description
### The dataset consist of 7 features.
- Date           – The date of the stock movement
- Open           – The last trading price recorded when the market is open on the day
- Close          – The last trading price recorded when the market closes on that day
- High           –  Maximum prices that people had paid for the stock
- Low            –  Minimum prices that people has paid for the stock
- Adjacent Close –  Stock values are stated in terms of the closing price and the adjusted closing price. The closing price is the raw price, which is just the cash value of the last transacted price before the market closes. 
                    The adjusted closing price factors in anything that might affect the stock price after the market closes.
- Volume         – Shows the total number of shares traded for the day.

## Conceptual Framework
The framework of this project is designed in five stages where the dataset is pre-processed according to the problem’s need. The working of this application starts from the main.py file.
The first stage is to scrape the dataset from the website which consist of historical stock prices. The second stage is to dump the dataset into the database, and the accessibility of the data will only be from the database. The third stage is to fetch the dataset from the database and intrude it to the preprocessing.py file. The fourth stage is to retrieve the final pre-processed dataset and generate financial report for the dataset by using the reports.py file. The fifth stage is to deploy them as an application using flask Api.

|Stocks
|-----
+-------LOGGER.PY
+--------MAIN.PY
+--------STOCKS_SCRAPER.PY
+--------DB.PY
+--------DIRECTORY_OPPS.PY
+--------REPORTS.PY                             
+---------CONTENT.PY

## Methodology
The methodology implemented on this paper is done in four stages as data collection or scraping, Accessibility of data from server, validation and pre-processing of the dataset obtained from the server, finally generating reports with the help of statistical analysis, machine-learning techniques.

### Data Collection
The data required here is the historical stock data, which is extracted from the yahoo finance website using Beautiful soup library (Bs4). The available features for analysis are the ‘Date’,’Open’,’Close’,’High’,’Low’,’Adjacent Close’, ‘Volume’.

### Dumping Data to Server
MYSQL databases is used in order to back up the historical data in the database and then revive them accordingly. This application is designed in an abstract manner where we can search any company of interest. For example purposes the dataset that is dumped into the server is shown as below. The accessibility of the dataset will be only from the server.
 

