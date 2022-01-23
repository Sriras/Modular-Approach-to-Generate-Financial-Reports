import mysql.connector as connections
from Logger import logger_app
import csv


# initially we are establishing the database connection
class Database_Operations:
    '''
    The Data base operation

    written by - Sahasranaman Sriraman

    revision - None

    Version - 1.0
    '''
    column_name={'Date':'varchar(20)','Open':'decimal(20,10)','High':'decimal(20,10)','Low':'decimal(20,10)','Close':'decimal(20,10)','Adjclose':'decimal(20,10)','Volume':'int(20)'}
    def __init__(self,file_name,localhost='localhost',password='Bullseye~12345',database_name=None,user='root',Table_name=None):
        self.localhost=localhost
        self.password=password
        self.database=database_name
        self.user=user
        self.logger=logger_app
        self.Tablename=Table_name
        self.filename=file_name

    def init_database(self):
        return self.database

    def show_databases(self):
        self.logger('Entered the show_database object of the database operation class').Logger()
        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=self.database)
            cursor=mydb.cursor()
            querry='show databases;'
            cursor.execute(querry)
            data=[i for i in cursor.fetchall()]
            return data
        except Exception as e:
            self.logger('Failed to fetch the databases,Came out of the show_database object').Logger(),print(e)


    def create_databases(self):
        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password)
            cursor = mydb.cursor()
            querry='create database'+' '+ self.database+';'
            cursor.execute(querry)
        except Exception as e:
            self.create_tables()
        else:
            self.create_tables()
    def drop_databases(self,database_name):
        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password)
            querry = 'drop database' + ' ' + database_name + ';'
            cursor = mydb.cursor()
            cursor.execute(querry)
        except Exception as e:
            print(e)

    def Connection_establishment(self):
        self.logger('Entered the connection_establishment object of the Databaseoperation class').Logger()

        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=self.database)
            print(mydb.is_connected(), 'Connection Established Succesfully')
        except Exception as e:
            self.logger('The connection failed')

    def create_tables(self):
        for elem in self.column_name.keys():
            val=self.column_name[elem]
            try:
                mydb=connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=self.database)
                querry='ALTER TABLE {Table_name} ADD {column_name} {dataType}'.format(Table_name=self.Tablename,column_name=elem,dataType=val)
                cursor=mydb.cursor()
                cursor.execute(querry)
            except Exception as e:
                mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=self.database)
                querry='CREATE TABLE {Table_name}({column_name} {datatype})'.format(Table_name=self.Tablename,column_name=elem,datatype=val)
                cursor=mydb.cursor()
                cursor.execute(querry)
            continue
        else:
            self.dump_to_database()

    def dump_to_database(self):
        try:
            mydb=connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=self.database)
            d=open(self.filename, 'r')
            header=d.readline()
            data = csv.reader(d)
            for line in enumerate(data):
                cursor = mydb.cursor()
                cursor.execute('insert into' + ' ' + self.Tablename + ' ' + 'values{};'.format(tuple([(line[1][0])]+ [float(elem) if elem!='null' else 0 for elem in line[1][1:]])))
        except Exception as e:
            print(e)
        else:
            mydb.commit()

    def workwith_database(self,database_name):
        while True:
            try:
                mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password,database=database_name)
                sql_querries=str(input('Generate manual querries '))
                if sql_querries=='stop':
                    break
                else:
                    cursor = mydb.cursor()
                    cursor.execute(sql_querries)
                    for i in cursor.fetchall():
                        print(i)
            except Exception as e:
                print(e)

    def insert_records(self,database_name,table_name,values):
        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password, database=database_name)
            print(mydb.is_connected(),'Connected')
        except Exception as e:
            print(e)
        else:
            Querry='insert into'+' '+table_name+'values{}'.format(tuple(values))
            cursor=mydb.cursor()
            cursor.execute(Querry)
            mydb.commit()

    def Close_connection(self):
        try:
            mydb = connections.Connect(host=self.localhost, user=self.user, passwd=self.password)
            mydb.close()
        except Exception as e:
            print(e)
        else:
            print('DATABASE CONNECTION CLOSED')


