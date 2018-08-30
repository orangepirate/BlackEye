import pymysql

class MySqlCommand(object):
    # initialization
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = 'geniusjohn'
        self.db = 'blackEye'
    # connect to database
    def connectMySql(self):
        try:
            self.conn = pymysql.connect(self.host,self.port,self.user,self.password,self.db,charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)