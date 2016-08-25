
class _const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


const = _const()
const.ENCODE_FORM = 'UTF-8'
const.HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 '
                                   '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

const.DISTRICTS = ['luohu', 'futian', 'nanshan', 'yantian', 'baoan', 'longgang', 'longhuaxinqu', 'guangmingxinqu',
                  'pingshanxinqu', 'dapengxinqu']
const.ERSHOU = 'ershoufang'
const.URL_ERSHOU = 'http://sz.lianjia.com/ershoufang/'
const.TB_ERSHOU = 'TB_ERSHOU'

const.DEAL = 'chengjiao'
const.URL_DEAL = 'http://sz.lianjia.com/chengjiao/'
const.TB_DEAL = 'TB_DEAL'

const.DB_USER = 'root'
const.DB_PASSWORD = 'root'
const.DB_ADRESS = 'localhost:3306'
const.DB_LIANJIA = 'DB_LIANJIA'


const.UNIT_PRICE = '单价'
