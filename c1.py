#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: Michael Guo
# create_time: 2019/12/17 22:07

# import requests
import random
import re


# from bs4 import BeautifulSoup

def demo_string():
    stra = 'hello word'
    print(stra.capitalize())
    print(stra.replace('word', 'nowcoder'))
    strb = '\n\rhello nowcoder \r\n'
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    strc = 'hello w'
    print(3, strc.startswith('hel'))
    print(4, strc.endswith('w'))
    print(5, stra + strb + strc)
    print(6, len(strc))
    print(7, '-'.join(['a', 'b', 'c']))
    print(8, strc.split(' '))
    print(9, strc.find('ello'))


def demo_operation():
    print(1, 1 + 2, 5 / 2, 5 * 2, 5 - 2)
    print(2, True, not True)
    print(3, 1 > 2, 5 < 2)
    print(4, 2 << 3)
    print(5, 5 | 3, 5 & 3, 5 ^ 3)
    x = 2
    y = 3.3
    print(x, y, type(x), type(y))


def demo_buidinfunction():
    print(1, max(1, 2), min(2, 5))
    print(2, len('xxx'), len('[1,2,3]'))
    print(abs(-2))  # fabs ,Math.fabs
    print(4, range(1, 10, 3))
    print(5, dir(list))
    x = 2
    print(6, eval('x+3'))
    print(7, chr(97), ord('a'))
    print(8, chr(65), ord('A'))
    print(9, divmod(11, 3))


def demo_controlflow():
    score = 65
    if score > 99:
        print(1, 'A')
    elif score > 60:
        print(2, 'B')
    else:
        print(3, 'C')

    while score < 100:
        print(score)
        score += 10

    score = 65

    # continue , break , pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_special
        if i < 5:
            continue
        print(3, i)
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]
    print(1, lista)
    listb = ['a', '1', 'c', '1.1']
    print(2, listb)
    lista.extend(listb)
    print(3, lista)
    print(4, len(lista))
    print(5, 'a' in listb)
    lista = lista + listb
    print(6, lista)
    listb.insert(0, 'www')
    print(7, listb)
    # listb.top(1)
    # print(8,listb)
    listb.reverse()
    print(9, listb)
    print(10, listb[0], listb[1])
    listb.sort()
    print(11, listb)
    listb.sort(reverse=True)
    print(12, listb)
    print(13, listb * 2)
    print(14, [0] * 14)

    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print(15, listaa)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print(1, dicta)
    print(2, dicta.keys(), dicta.values())
    for key, value in dicta.items():
        print('key-value', key, value)
    dictb = {'+': add, '-': sub}
    print(4, dictb['+'](1, 2))
    print(5, dictb.get('-')(15, 3))
    dictb['*'] = 'x'
    print(dictb)
    dicta.pop(4)
    print(dicta)
    del dicta[1]
    print(7, dicta)


def demo_set():
    seta = ((1, 2, 3))
    setb = ((2, 3, 4))
    print(1, seta)
    print(2, setb)
    print(3, seta + setb)
    # print(4, seta - setb)
    print(4, len(seta))
    print(5, seta | setb)


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'i am' + ' ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'i am' + ' ' + self.name + ' ' + str(self.uid) + ' ' + self.group


class Guest(User):
    def __repr__(self):
        return 'i am' + ' ' + self.name + ' ' + str(self.uid)


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)


def demo_exception():
    try:
        print(2 / 1)
        print(2 / 0)
        raise Exception('Raise Error', 'NewCoder')
    except Exception as e:
        print('error:', e)

    finally:
        print('clear up')


def demo_random():
    # random.seed(1)
    # 0-1 float
    print(1, random.random())
    # 0-100 int
    print(2, int(random.random() * 100))
    print(3, random.randint(1, 100))
    print(4, random.choice(range(0, 100, 10)))
    print(5, random.sample(range(0, 100), 4))
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(6, a)


def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('\d')
    p2 = re.compile('[\d]+')
    print(1, p1.findall(str))
    print(2, p2.findall(str))

    str1 = 'a@163.com;b@gmial.com;c@qq.com;e@163.com;z@qq.com'
    p3 = re.compile('[\w]+@163\.com')
    p4 = re.compile('[\w]+@[163|qq]+\.com')
    print(3, p3.findall(str1))
    print(4, p4.findall(str1))

    str2 = '<html><h>title</h><body>xxxx</body></html>'
    p5 = re.compile('<h>[^<]+</h>')
    p6 = re.compile('<h>([^<]+)</h>')
    p7 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print(5, p5.findall(str2))
    print(6, p6.findall(str2))
    print(7, p7.findall(str2))

    str3 = 'xx2016-06-11yy'
    p8 = re.compile('\d\d\d\d-\d\d-\d\d')
    p9 = re.compile('\d{4}-\d{2}-\d{2}')
    print(p8.findall(str3))
    print(p9.findall(str3))


if __name__ == '__main__':
    # print('hello nowcoder')
    # demo_string()
    # demo_operation()
    # demo_buidinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    '''
    user1 = User('u1', 1)
    print(user1)
    admin1 = Admin('a1', 101, 'g1')
    print(admin1)
    print(create_user('USERX'))
    demo_exception()
    '''
    # demo_random()
    demo_re()
