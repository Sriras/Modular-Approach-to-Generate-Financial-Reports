
class Message:
    def Introduction(self):
        with open('Introduction','r') as file:
            return  file.read()
    def Visuals(self):
        return 'VISUVALIZATION'

    def Spread(self):
        with open('Spread', 'r') as file:
            return file.read()
    def volatility(self):
        with open('Volatility','r') as file:
            return file.read()
    def returns(self):
        with open('Returns','r') as file:
            return file.read()
    def moving_average(self):
        with open('Moving_average', 'r') as file:
            return file.read()
    def auto_correlation(self):
        with open('AutoCorrelation','r') as file:
            return file.read()
    def lstm(self):
        with open('lstm','r') as file:
            return file.read()
