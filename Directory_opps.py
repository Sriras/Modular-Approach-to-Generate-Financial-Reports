import os
from Logger import logger_app
import shutil

class dir_opps:
    '''
    The dir_opps is a class which is cretaed inorder to have control within the current working directory

    written by : Sahasranaman Sriraman

    revision - none

    version - 1.0

    '''

    def __init__(self,stock_name,company_name,path_csv='C:\\Users\\sahas\\PycharmProjects\\Stocks\\',path_diropps = r'C:\Users\sahas\PycharmProjects\Stocks'):
        self.path = path_csv+stock_name
        self.path_dir_opps = path_diropps
        self.stock_string = stock_name
        self.companyname = company_name
    def rm_dir(self):
        '''
        The rm_dir method is used to remove the files from the directory

        written by - Sahasranaman Sriraman

        revision -none

        version - 1.0
        '''
        logger_app('Entered into the rm_dir object of the dir_opps class').Logger()
        try:
            os.remove(self.path)
        except Exception as e:
            logger_app('Something went wrong in the rm_dir object of the dir_opps class')
        else:
            logger_app('rm_dir opps sucesfull. Here after stock data will be access only by the database').Logger()
    def Move_file(self):
        '''
                The rm_dir method is used to move the files to a directory

                written by - Sahasranaman Sriraman

                revision -none

                version - 1.0
                '''
        logger_app('Entered into the Move_file method of the dir_opps class')
        try:
            file_to_move=os.path.join(self.path_dir_opps,self.companyname+'.docx')
            shutil.move(file_to_move,os.path.join(self.path_dir_opps,'Financial_Report'))
        except Exception as e:
            print(e)
        else:
            logger_app('File sucesfully moved to the required directory')
