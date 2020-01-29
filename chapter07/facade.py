"""
The Facade Pattern (外观模式: 简化复杂对象的访问问题)
外观模式用来简化复杂系统的访问。通过简化的接口只访问需要的部分，隐藏系统复杂性。
想象一下公司接线员，虽然公司内部运行机制比较复杂，但是接线员可以迅速帮你解决特定问题。

我们以实现个简单的操作系统示例说明外观模式：
"""
from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    """
    Abstract Base Class 
    """
    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        '''actions required for initializing the file server'''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        '''actions required for booting the file server'''
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        '''actions required for killing the file server'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''check validity of permissions, user rights, etc.'''
        print(
            f"trying to create the file '{name}' for user '{user}' with permissions {permissions}"
        )


class ProcessServer(Server):
    def __init__(self):
        '''actions required for initializing the process server'''
        self.name = 'ProcessServer'
        self.state = State.new
        print(State._member_map_)

    def boot(self):
        print(f'booting the {self}')
        '''actions required for booting the process server'''
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        '''actions required for killing the process server'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''check user rights, generate PID, etc.'''
        print(f"trying to create the process '{name}' for user '{user}'")


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    '''The Facade 
    实现外观模式，外部使用的代码不必知道 FileServer 和 ProcessServer的
    内部机制，只需要通过OperatingSystem类调用'''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        """
        access file system
        """
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()
