"""
The Flyweight Pattern (享元模式: 实现对象复用从而改善资源使用）
OOP编程中容易出现对象创建带来的性能和内存占用问题，需要满足以下条件：

1. 需要使用大量对象(python里我们可以用__slots__节省内存占用)
2. 对象太多难以存储或解析大量对象。
3. 对象识别不是特别重要，共享对象中对象比较会失败。
"""
import random
from enum import Enum

CarType = Enum('CarType', 'subcompact compact suv')


class Car:
    __slots__ = ('car_type',)
    pool = dict()

    def __new__(cls, car_type):
        print(f'car_type: {car_type}')
        obj = cls.pool.get(car_type)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        type = self.car_type
        msg = f'render a car of type {type} and color {color} at ({x}, {y})'
        print(msg)


def main():
    rnd = random.Random()
    #age_min, age_max = 1, 30    # in years
    colors = 'white black silver gray red blue brown beige yellow green'.split()
    min_point, max_point = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarType.subcompact)
        c1.render(random.choice(colors), rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(3):
        c2 = Car(CarType.compact)
        c2.render(random.choice(colors), rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(5):
        c3 = Car(CarType.suv)
        c3.render(random.choice(colors), rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    print(f'cars rendered: {car_counter}')
    print(f'cars actually created: {len(Car.pool)}')

    c4 = Car(CarType.subcompact)
    c5 = Car(CarType.subcompact)
    c6 = Car(CarType.suv)
    print(f'{id(c4)} == {id(c5)}? {id(c4) == id(c5)}')
    print(f'{id(c5)} == {id(c6)}? {id(c5) == id(c6)}')


if __name__ == '__main__':
    main()
