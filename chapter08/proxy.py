"""
The Proxy Pattern(代理模式：通过一层间接保护层实现更安全的接口访问）
在访问真正的对象之前做一些操作。有四种常用的代理类型:

A remote proxy.使得访问远程对象就像本地访问一样，例如网络服务器。隐藏复杂性，使得访问本地远程统一。比如ORM
A virtual proxy. 用来实现延迟访问，比如一些需要复杂计算的对象，python里可以实现lazy_property，性能改善
A protection/protective proxy. 控制敏感对象的访问，加上一层保护层，实现安全控制
A smart(reference) proxy. 访问对象时加上一层额外操作，例如引用计数和线程安全检查。weakref.proxy()
"""
import abc


class SensitiveInfo(metaclass=abc.ABCMeta):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def add(self, user):
        pass


class Info(SensitiveInfo):
    '''protection proxy to SensitiveInfo'''
    def __init__(self):
        super().__init__()
        # self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        """ 给add操作加上密钥验证，保护add操作 """
        sec = input('what is the secret? ')
        self.users.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    main()
