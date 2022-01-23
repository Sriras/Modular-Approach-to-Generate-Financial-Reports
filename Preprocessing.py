import pandas as pd
from Logger import logger_app
import sqlalchemy
from DB import Database_Operations


class validation:

    def __init__(self,stockname,company_name,engine='mysql+pymysql://root:Bullseye~12345@localhost/{}'.format(Database_Operations(database_name='financialdata',file_name=None).init_database())):
        self.logger=logger_app
        self.engine=engine
        self.stock_name=stockname
        self.companyname=company_name

    def DataPreprocessing(self):
        self.logger('Entered the check_null method  of the Valiation class').Logger()
        try:
            Engine=sqlalchemy.create_engine(self.engine)
            data_frame=pd.read_sql_table(self.stock_name.split('.')[0],Engine)
        except Exception as e:
            self.logger('Something went wrong in the Check_null object of the validate class').Logger()
        else:
            self.logger('Checking the null values in the dataframe').Logger()
            try:
                self.logger('The shape of rows and columns before droping -- {}'.format(data_frame.shape))
                data_frame.drop(index=data_frame[data_frame['Volume']==0].index,inplace=True,axis=0)
                data_frame.reset_index(drop=True)
                data_frame.to_csv(r'C:\\Users\\sahas\\PycharmProjects\\Stocks\\{}'.format(self.stock_name + '_validated_.csv'))
            except Exception as e:
                print(e)

