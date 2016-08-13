import mysql.connector
import Cons

class DBProvider(object):

    def db_conn(self):
        self.conn = mysql.connector.connect(user=Cons.DB_USER, password=Cons.DB_PASSWORD, database=Cons.DB_LIANJIA)
        return self.conn

    def db_close(self):
        if (self.conn != None):
            self.conn.close()

    def exec_sql(self, sql):
        try:
            if (self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise mysql.connector.Error('Connection Error')

            cursor.execute(sql)
            return cursor.rowcount
        except mysql.Error:
            print('')

    def add_ershou(self, data):
        try:
            if (self.conn is not None):
                cursor = self.conn.cursor()
            else:
                raise mysql.connector.Error('Connection Error')

            sql = '''insert into TB_ERSHOU (name, date, total_price, unit_price, url, bedroom, livingroom, area,
                 toward, fitment, follows, visit_times, pub_date, remarks) values ('%s', NOW(),'%s','%s', '%s','%s','%s','%s',
                 '%s','%s','%s','%s','%s','%s')''' % (data['name'], data['total_price'], data['unit_price'], data['url'], data['bedroom'],
                    data['livingroom'], data['area'], data['toward'], data['fitment'],
                    data['follows'], data['visit_times'], data['pub_date'], data['remarks'])
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error(''):
            self.conn.rollback()
