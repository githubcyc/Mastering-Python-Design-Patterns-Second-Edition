"""
The Adapter Pattern(适配器模式: 解决接口不兼容问题)
开始介绍结构型设计模式，结构型设计模式通过组合对象来实现新功能。
适配器模式通过引入间接层来实现不兼容接口之间的适配。
现实中最好的例子就是手机充电口，不同型号安卓手机都可以用同样的充电线充电。
在python中可以通过继承实现适配，也可以通过使用class的__dict__属性。
开闭原则：适配器模式和OOP中的开闭原则关系密切，开闭原则强调对扩展开放，对修改关闭。
我们可以通过创建适配器模式在不修改原有类代码的情况下实现新的功能。
"""
from external import Musician, Dancer


class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return 'hires an artist to perform for the people'


class Adapter:
    def __init__(self, obj, adapted_methods):
        """
        adapted_methods -> organize_event
        """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():

    objects = [
        Club('Jazz Cafe'),
        Musician('Roy Ayers'),
        Dancer('Shane Sparks')
    ]

    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj, 'play'):
                adapted_methods = dict(organize_event=obj.play)
            elif hasattr(obj, 'dance'):
                adapted_methods = dict(organize_event=obj.dance)

            # referencing the adapted object here
            obj = Adapter(obj, adapted_methods)

        print(f'{obj} {obj.organize_event()}')
        print(obj.__dict__)


if __name__ == "__main__":
    main()
