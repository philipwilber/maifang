
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

const.ERSHOU = 'ershoufang'
const.DEAL = 'chengjiao'
const.URL_ERSHOU = 'http://sz.lianjia.com/ershoufang/'
const.URL_DEAL = 'http://sz.lianjia.com/chengjiao/'

const.DB_USER = 'root'
const.DB_PASSWORD = 'root'
const.DB_ADRESS = 'localhost:3306'
const.DB_LIANJIA = 'DB_LIANJIA'
const.TB_ERSHOU = 'TB_ERSHOU'
const.TB_DEAL = 'TB_DEAL'

const.UNIT_PRICE = '单价'
