"""
The Decorator Pattern(装饰器模式： 无需子类化实现扩展对象功能问题)
通常给一个对象添加新功能有三种方式：
1. 直接给对象所属的类添加方法
2. 使用『组合』
3. 使用『继承』，优先使用组合而非继承

装饰器模式提供了第四种选择，通过动态改变对象扩展对象功能。
其他编程语言通常使用继承实现装饰器装饰器模式，而python内置了装饰器。
装饰器有很多用途，比如数据校验，事务处理，缓存，日志等。
比如用装饰器实现一个简单的缓存，python3.5自带了functools.lru_cache
"""
import functools 
 
def memoize(fn): 
    cache = dict() 
 
    @functools.wraps(fn) 
    def memoizer(*args): 
        if args not in cache: 
            cache[args] = fn(*args) 
        return cache[args] 
 
    return memoizer
    
@memoize 
def number_sum(n): 
    '''Returns the sum of the first n numbers''' 
    assert(n >= 0), 'n must be >= 0' 
    if n == 0:
        return 0
    else:
        return n + number_sum(n-1)
 
@memoize 
def fibonacci(n): 
    '''Returns the suite of Fibonacci numbers''' 
    assert(n >= 0), 'n must be >= 0'
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)    
        
def main():
    from timeit import Timer

    to_execute = [
        (number_sum, 
         Timer('number_sum(300)', 'from __main__ import number_sum')),
        (fibonacci, 
         Timer('fibonacci(100)', 'from __main__ import fibonacci'))    
    ]
    
    for item in to_execute:
        fn = item[0]
        print(f'Function "{fn.__name__}": {fn.__doc__}')
        t = item[1]
        print(f'Time: {t.timeit()}')
        print()

if __name__ == '__main__': 
    main()
