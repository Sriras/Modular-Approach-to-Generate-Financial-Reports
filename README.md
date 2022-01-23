# MODULAR APPROCH TO GENERATE FINANCIAL REPORTS (AN END TO END APPLICATION)

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
- sqlalchemy
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
 
![db img](https://user-images.githubusercontent.com/93818265/150693118-325330fc-caf5-45a3-8574-e4b282cce780.png)

### Validation and Pre-processing of the dataset
Once the dataset is dumped into the server, the accessibility of the dataset is only from the server. The application is programed in such a way that the schema  is automatically created. The dataset is revived from the server and is imposed to the preprocessing.py file in order to check whether entire features are available and there are no null values. The obtained validated file will be the finalized one where we will implement our Statistical Measures and Machine Learning techniques. The validated file will be saved in the directory where the python application runs. Here is the image of the validated file.

![validated py](https://user-images.githubusercontent.com/93818265/150693348-85bcb0e1-16a5-4910-b578-148fff54ed3e.png)

### Generating Reports 
Once the validated file is obtained, the idea of this project is to generate financial report about the company and derive customer’s interest to buy the stocks. These financial report speaks about the historical performance of the company and as we have mentioned this will be an abstract application the information about the company will be shared according the period of interest which is a parameter grabbed while input.


![gui](https://user-images.githubusercontent.com/93818265/150693525-0c5b4bd1-d208-45cd-88e9-6243f67737f5.png)



|Methods| Explanation|
|-------|-------------|
Visualization                |This will explain the visuals in graphs according to the users period of interest and visualization will be done year wise
Spread                       |Spread calculates the difference between two prices or rates. Here it considers the opening and closing value of the stock. Zscore analysis is applied to the    spread attribute, which will be very significant to measure the fluctuation in the stocks. Spread = High – Low.|
Volatility                   | Volatility is a statistical measure of the dispersion of returns for a given security or market index. In most cases, the higher the volatility, the riskier the security. Volatility is often measured as either the standard deviation or variance between returns from that same security or market index.
Daily Returns                | The returns are the daily returns, which is calculated by the closing value of the next day divided by the closing value of the current day. Return = previous close / current close.
Moving Average               | Moving average is a technique, which is used to analyze the data by forming a series of average of subsets of the dataset. The Moving average will help to smoothen the curve by constantly updating the average price.
Auto-correlation Plots       | The Auto – correlation plots or the correlation plots is used in order to find out the seasonality or the pattern of a particular feature, which paves way for the analysis to further make keen decision.
LSTM (Long Short Term Memory) | The LSTM (Long Short Term Memory) is an Artificial Neural Network Architecture, which is used to process multiple data points as sequence and predict the next value .LSTM is used to Predict the stock price.




## Output
As discussed earlier, this application will be an abstract one which can be used to generate financial reports for the company of interest and the information from the analysis will be exhibited to the user in order for investing in stock market. Let us assume the company of interest at random and period of interest for 6 years.



![Screenshot (44)](https://user-images.githubusercontent.com/93818265/150695695-ae026868-3444-467e-9db2-294530e41d34.png)


![Screenshot (35)](https://user-images.githubusercontent.com/93818265/150695365-76e9411c-b0c7-4280-9fd6-bd3d4f28b0da.png)


![Screenshot (37)](https://user-images.githubusercontent.com/93818265/150695395-9b1521f0-3985-480e-a137-cc62a89e0e04.png)


![Screenshot (36)](https://user-images.githubusercontent.com/93818265/150695402-97bc7a86-8365-4666-977d-811f0bce0f77.png)


![Screenshot (41)](https://user-images.githubusercontent.com/93818265/150695534-79a2fb9a-0f3f-439d-af44-626af4d756a1.png)


![Screenshot (42)](https://user-images.githubusercontent.com/93818265/150695599-c0068ea6-0382-4c9a-8417-d9d1bb178aa5.png)






# Software Requirments
-Python version 3.9.0 or above


# How to run the Code
```
$ python main.py
```



