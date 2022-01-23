from datetime import datetime
class logger_app():
    '''
    The logger_app class is built in order to calculate the runtime of the program,errors while runtime.

    written by - Sahasranaman Sriraman

    revision - none

    version - 1.0
    '''

    def __init__(self,log_message):
        self.message=log_message
    def Logger(self):
        '''
         The logger method is built in order to calculate the runtime of the program,errors while runtime.

         written by - Sahasranaman Sriraman

         revision - none

         version - 1.0
         '''

        self.time=datetime.now()
        self.date=self.time.date()
        self.currentTime=self.time.strftime("%H:%M:%S")
        f=open('logger_info','a+')
        return f.write("Date -- {} , Current_time -- {} ,log message -- {}\n".format(self.date,self.currentTime,self.message))
