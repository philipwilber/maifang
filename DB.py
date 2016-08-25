import mysql.connector
from consts import const


class DBProvider(object):

    def db_conn(self):
        self.conn = mysql.connector.connect(user=const.DB_USER, password=const.DB_PASSWORD, database=const.DB_LIANJIA)
        return self.conn

    def db_close(self):
        if (self.conn is not None):
            self.conn.close()

    def exec_sql(self, sql):
        try:
            if (self.conn is not None):
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

            sql = '''insert ignore into TB_ERSHOU (url_id, name, date, total_price, unit_price, bedroom, livingroom, area,
                 toward, fitment, follows, visit_times, pub_date, district, remarks) values ('%s','%s', NOW(),'%s','%s','%s','%s',
                 '%s','%s','%s','%s','%s','%s','%s','%s')''' % (
                data['url_id'], data['name'], data['total_price'], data['unit_price'], data['bedroom'],
                data['livingroom'], data['area'], data['toward'], data['fitment'],
                data['follows'], data['visit_times'], data['pub_date'], data['district'], data['remarks'])
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error(''):
            self.conn.rollback()

    def add_deal(self, data):
        try:
            if (self.conn is not None):
                cursor = self.conn.cursor()
            else:
                raise mysql.connector.Error('Connection Error')

            sql = '''insert ignore into TB_DEAL (url_id, name, date, total_price, unit_price, bedroom, livingroom, area,
                 toward, fitment, floor, deal_date) values ('%s', '%s', NOW(),'%s','%s','%s','%s','%s',
                 '%s','%s','%s', '%s')''' % (
                data['url_id'], data['name'], data['total_price'], data['unit_price'], data['bedroom'],
                data['livingroom'], data['area'], data['toward'], data['fitment'], data['floor'], data['deal_date'])
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error(''):
            self.conn.rollback()
