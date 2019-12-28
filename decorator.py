#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: Michael Guo
# create_time: 2019/12/28 19:01

def log(func):
    '''
    *有名字的参数，**无名字的参数
    :param func:
    :return:
    '''

    def wrapper(*args, **kvargs):
        print("before calling", func.__name__)
        print('args', args, 'kvargs', kvargs)
        func(*args, **kvargs)
        print("end calling", func.__name__)

    return wrapper


@log
def hello(name, age):
    print('hello', name, age)


if __name__ == '__main__':
    # hello('nowcoder', 2)
    hello(name='nowcoder', age=2)
