import pickle
from sqlalchemy import create_engine, Column, Integer, String, DATE, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

connstr = "{}://{}:{}@{}:{}/{}".format(
    'mysql+pymysql', 'root', '', '191.168.19.196',
    3306, 'test'
)
engine = create_engine(connstr, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Atm(Base):
    __tablename__ = 'atm'
    name = Column(String(50), primary_key=True)
    password = Column(String(64), nullable=False)
    bank = Column(String(50), nullable=False, default='ICBC')
    amount = Column(Integer, nullable=False)
    record = Column(String(255))
    time = Column(DATE)

    def __repr__(self):
        return '{} 用户名：{} 余额：{}'.format(
            self.bank, self.name, self.amount
        )


class Sql:

    def select(self, name):
        slt_result = session.query(Atm).filter(Atm.name == name)
        return slt_result

    def update_pw(self, name, password):
        result = self.select(name)
        for p in result:
            p.password = password
            session.add(p)
            session.commit()

    def update_amount(self, name, amount):
        result = self.select(name)
        for i in result:
            i.amount = i.amount + amount
            if i.amount >= 0:
                session.add(i)
                session.commit()
            else:
                print('余额不足')
                session.rollback()
            print('{} 的余额为 {}'.format(name, i.amount))

    def insert(self, name, pw, amount=5000):
        info = Atm(name=name, password=pw, amount=amount)
        session.add(info)
        session.commit()

    def delete(self, name):
        result = self.select(name)
        for a in result:
            session.delete(a)
            session.commit()


class AtmServer():

    def __init__(self, names):
        self.names = names
        self.sql = Sql()

    def show_info(self, result):
        for i in result:
            return i

    def registered(self):  # 用户注册
        username = input('请输入用户名： ')
        if ('{}'.format(username),) not in self.names: #判断用户是否存在
            pw = input('请输入密码: ')
            self.sql.insert(username, pw)    #添加用户
            print('注册成功，当前用户为 {}，余额 {}元'.format(username, 5000))
        else:
            print('用户已存在！')

    def user_menu(self, username):    #用户菜单
        print('---------------------------------------------')
        print('----0-----------------------------查询余额----')
        print('----1-----------------------------存    钱----')
        print('----2-----------------------------取    钱----')
        print('----3-----------------------------转    账----')
        print('----4-----------------------------修改密码----')
        print('----5-----------------------------注    销----')
        print('----6-----------------------------退    出----')
        print('---------------------------------------------')
        number1 = int(input('请根据提示输入数字: '))
        if number1 == 0:  # 查询余额
            result = self.sql.select(username)
            print(self.show_info(result))
            return self.user_menu(username)
        if number1 == 1:  # 存钱
            amount = int(input('请输入要存入的金额： '))
            self.sql.update_amount(username, amount)
            return self.user_menu(username)
        if number1 == 2:  # 取钱
            amount = -int(input('请输入要存入的金额： '))
            self.sql.update_amount(username, amount)
            return self.user_menu(username)
        if number1 == 3:  #转账
            other_user = input('输入要转入的账户')
            if ('{}'.format(other_user),) in names:
                _amount = int(input('要转入的金额： '))
                self.sql.update_amount(username, -_amount)
                self.sql.update_amount(other_user, _amount)
            else:
                print('该用户不存在')
            return self.user_menu(username)
        if number1 == 4:  # 修改密码
            new_pw = input('输入新密码： ')
            self.sql.update_pw(username, new_pw)
            return self.menu()
        if number1 == 5:  # 注销用户
            self.sql.delete(username)
            return self.menu()
        if number1 == 6:  # 返回上级菜单
            return self.menu()

    def pw_authentification(self, username):
        result = self.sql.select(username)
        password = self.show_info(result)
        for i in range(3):
            pw = input('输入密码： ')
            if pw == password.password:
                return self.user_menu(username)
            else:
                print('密码错误，还有{}次机会'.format(2-i))
                continue
        else:
            print('退出')


    def menu(self):
        global flag
        print('欢迎使用爱存不存ATM虚拟系统')
        print('---------------------------------------------')
        print('----0-----------------------------注    册----')
        print('----1-----------------------------登    录----')
        print('----2-----------------------------退    出----')
        print('---------------------------------------------')
        num = input('请根据提示输入： ')

        try:
            if num == '0':
                user.registered()
            if num == '1':
                username = input('请输入用户名： ')
                if ('{}'.format(username),) not in names:
                    print('用户不存在， 请先创建')
                    user.registered()
                else:
                    user.pw_authentification(username)
            if num == '2':
                flag = False
                print('欢迎下次使用')
            if num not in ('0', '1', '2'):
                print('输入错误，请根据提示输入!')
        except:
            print('~~~~~~~输入错误')





if __name__ == '__main__':
    flag = True
    names = session.query(Atm.name)
    user = AtmServer(names)
    while flag:
        user.menu()


