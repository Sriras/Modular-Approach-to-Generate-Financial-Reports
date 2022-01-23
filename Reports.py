import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
import time
from sklearn.preprocessing import MinMaxScaler
import statsmodels.api as sm
from keras.models import Sequential
from keras.layers import Dense,LSTM

class PriorTOdoc():
    def __init__(self,validated_data,company_name):
        self.validated=validated_data
        self.companyName=company_name
        self.Data_frame = pd.read_csv(self.validated)
    def Segregation(self):
        try:
            Data_frame=self.Data_frame
            Data_frame['Year']=[yrs.split('-')[0] for yrs in Data_frame['Date']]
        except Exception as e:
            print(e)
        else:
            if len(list(Data_frame['Year'].unique()))>1:
                Frame_list=[]
                for year in list(Data_frame['Year'].unique()):
                    sub_frame=(Data_frame['Year'] == year)
                    Frame_list.append(Data_frame[sub_frame])
                return Frame_list
            else:
                Frame_list = []
                Frame_list.append(Data_frame[Data_frame['Year'] == list(Data_frame['Year'].unique())[0]])
                return Frame_list

    def Visuvalization(self):
        try:
            segregation=self.Segregation()
            if len(segregation) > 1:
                visuals=[]
                i=1
                for df in segregation:
                    df.plot.line(x='Date',y=['Open','Close','High','Low'])
                    plt.xlabel(df['Year'].unique()[0])
                    plt.ylabel('Open-Close-High-Low')
                    plt.savefig(self.companyName+'_vis{}.png'.format(i))
                    visuals.append(self.companyName+'_vis{}.png'.format(i))
                    plt.close()
                    i += 1
                else:
                    self.Data_frame.plot.line(x='Date',y=['Open','Close','High','Low'])
                    plt.ylabel('Open-Close-High-Low')
                    plt.savefig(self.companyName + '_entire.png')
                    visuals.append(self.companyName + '_entire.png')
                    plt.close()

                return visuals
            else:
                visuals=[]
                segregation[0][['Open','High','Low','Close']].plot()
                plt.xlabel(segregation[0].unique()[0])
                plt.ylabel('Open-Close-High-Low')
                plt.savefig(self.companyName+'_vis1.png')
                visuals.append(self.companyName+'_vis1.png')
                plt.close()
                return visuals
        except Exception as e:
            print(e)


    def Spread(self):
        try:
            Spread = self.Segregation()
            if len(Spread)>1:
                visuals=[]
                i=1
                for df in Spread:
                    Spread = df['High']-df['Low']
                    plt.plot(Spread,'*-g')
                    plt.xlabel(df['Year'].unique()[0])
                    plt.ylabel('High-Low')
                    plt.savefig(self.companyName+'_spread{}.png'.format(i))
                    visuals.append(self.companyName+'_spread{}.png'.format(i))
                    plt.close()
                    i += 1
                return visuals
            else:
                visuals = []
                df = pd.DataFrame(Spread[0])
                Spread = df['High']-df['Low']
                plt.plot(stats.zscore(Spread),'*-g')
                plt.xlabel(df['Year'].unique()[0])
                plt.ylabel('High-low')
                plt.savefig(self.companyName+'_spread1.png')
                visuals.append(self.companyName+'_spread1.png')
                plt.close()
                return visuals

        except Exception as e:
            print(e)


    def volatility(self):
        try:
            global_lst = []
            volatility = self.Segregation()
            message=''
            year = []
            std_dev = []
            if len(volatility)>1:
                for df in volatility:
                    spread = df['High']-df['Low']
                    message = message+'volatility for year {} : {}\n'.format(df['Year'].unique()[0], pd.DataFrame(spread).std().values[0])
                    year.append(int(df['Year'].unique()[0]))
                    std_dev.append(pd.DataFrame(spread).std().values[0])

            else:
                for df in volatility:
                    spread = df['High']-df['Low']
                    message = message+'volatility for year {} : {}'.format(df['Year'].unique()[0], pd.DataFrame(spread).std().values[0])

        except Exception as e:
            print(e)

        else:
            global_lst.append(message)
            global_lst.append(year)
            global_lst.append(std_dev)
            return global_lst

    def volatility_graph(self):
        try:
            visuals = []
            graph = self.volatility()
            x_coordinate = graph[1]
            y_coordinate = graph[2]
            plt.bar(x_coordinate,y_coordinate)
            plt.xlabel('Years')
            plt.ylabel('volatility count per year')
            plt.savefig(self.companyName+'_volatility_Bar_graph.png')
            plt.close()
            visuals.append(self.companyName+'_volatility_Bar_graph.png')
            return visuals

        except Exception as e:
            print(e)


    def Returns(self,volatility=251):
        try:
            global_list=[]
            visuals=[]
            daily_returns={}
            returns=self.Segregation()
            if len(returns)>1:
                iter=1
                for frame in returns:
                    previous,tomorrow=0,1
                    close=list(frame['Close'])
                    returns_per_day=[]
                    for val in range(len(close)-1):
                        returns_per_day.append(close[tomorrow]/close[previous])
                        previous+=1
                        tomorrow+=1
                    daily_returns[frame['Year'].unique()[0]] = returns_per_day
                    plt.plot(returns_per_day,'-.')
                    plt.xlabel(frame['Year'].unique()[0])
                    plt.ylabel('Daily returns')
                    plt.savefig(self.companyName+'_returns{}.png'.format(iter))
                    visuals.append(self.companyName+'_returns{}.png'.format(iter))
                    plt.close()
                    iter+=1

        except Exception as e:
            print(e)

        else:
            global_list.append(daily_returns)
            global_list.append(visuals)
            yearly_volatility=[]
            for key in daily_returns.keys():
                log_return=np.array([math.log(elem) for elem in daily_returns[key]]).std()
                yearly_volatility.append(log_return*(volatility**0.5))
            global_list.append(yearly_volatility)
            return global_list

    def returns_graph(self):
        try:
            visuals = []
            graph = self.Returns()
            x_coordinates = [int(elem) for elem in graph[0]]
            y_coordinates = graph[2]
            plt.bar(x_coordinates,y_coordinates)
            plt.xlabel('Years')
            plt.ylabel('Returns measure per year')
            plt.savefig(self.companyName+'_Returns_Bar_graph.png')
            visuals.append(self.companyName+'_Returns_Bar_graph.png')
            plt.close()
            return visuals

        except Exception as e:
            print(e)


    def dailyReturnvolatility(self):
        try:
            volatility=self.Returns()
            message=''
            data_frame = self.Data_frame
            data_frame['Year'] = [yrs.split('-')[0] for yrs in data_frame['Date']]
            i=0
            for elem in volatility[2]:
                message=message+'The  volatility of returns for year {} is {}\n'.format(data_frame['Year'].unique()[i],elem)
                i=i+1
            return message
        except Exception as e:
            print(e)

    def moving_average(self):
        try:
            visuals=[]
            data_frame=self.Data_frame
            data_frame['Mov_avg'] = data_frame['Close'].rolling(window=5, min_periods=2).mean()
            final_frame=data_frame.loc[1:,:]
            final_frame.plot.line(x='Date',y=['Close','Mov_avg'])
            plt.savefig(self.companyName+'_Moving_avg.png')
            time.sleep(10)
            visuals.append(self.companyName+'_Moving_avg.png')
            plt.close()
            return visuals

        except Exception as e:
            print(e)

    def correlation_plots(self,column='Close'):
        try:
            auto_corr_plt = []
            data_frame = self.Data_frame
            lag_order = data_frame.shape[0] - 300
            data_frame['seasonal_first_difference'] = data_frame[column] - data_frame[column].shift(250)
            sm.graphics.tsa.plot_acf(data_frame['seasonal_first_difference'].dropna(),lags= lag_order)
            plt.savefig(self.companyName+'_correlation plot.png')
            auto_corr_plt.append(self.companyName+'_correlation plot.png')
            plt.close()
            return auto_corr_plt
        except Exception as e:
            print(e)



    def LSTM(self, column='Close'):
        try:
            file_name = []
            data_frame = self.Data_frame
            data = data_frame.filter([column])
            # Convert the dataframe into a numpy array
            dataset = data.values
            # Number of rows to train the model
            training_data_len = math.ceil(len(dataset) * 0.8)
            # Scaling the dataset
            scaler = MinMaxScaler(feature_range=(0,1))
            scaled_data = scaler.fit_transform(dataset)
            # create the scaled training dataset
            train_data = scaled_data[0:training_data_len,:]
            # Split the data into x_train and y_train
            x_train = []
            y_train = []
            for i in range(100, len(train_data)):
                x_train.append(train_data[i-100:i,0])
                y_train.append(train_data[i,0])
                if i <= 101:
                    print(x_train,y_train)
            else:
                x_train_arr, y_train_arr = np.array(x_train), np.array(y_train)
                # Reshape the data
                x_train_arr = np.reshape(x_train_arr,(x_train_arr.shape[0], x_train_arr.shape[1],1))
                # Build LSTM model
                model = Sequential()
                model.add(LSTM(50,return_sequences=True,input_shape=(x_train_arr.shape[1],1)))
                model.add(LSTM(50, return_sequences=False))
                model.add(Dense(25))
                model.add(Dense(1))
                # Complie the model
                model.compile(optimizer='adam',loss='mean_squared_error')
                # Train the model
                model.fit(x_train_arr,y_train_arr,batch_size=1,epochs=1)
                # Create the testing dataset
                test_data = scaled_data[training_data_len - 100: , :]
                # Create the dataset x_test and y_test
                x_test = []
                y_test = dataset[training_data_len:,:]
                for elem in range(100, len(test_data)):
                    x_test.append(test_data[elem - 100:elem,0])
                # Convert the data into a numpy array
                x_test = np.array(x_test)
                # Reshape the data
                x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
                # The predicted price values
                predictions = model.predict(x_test)
                Predictions = scaler.inverse_transform(predictions)
                # rmse calculation
                rmse = np.sqrt(np.mean(predictions - y_test)**2)
                # plotting the dataset
                train = data[:training_data_len]
                validation = data[training_data_len:]
                validation['Predictions'] = Predictions
                # visualize the data
                plt.figure()
                plt.plot(train[column])
                plt.plot(validation[[column,'Predictions']])
                plt.savefig('Model_Prediction.png')
                file_name.append('Model_Prediction.png')
                return file_name

        except Exception as e:
            print(e)






