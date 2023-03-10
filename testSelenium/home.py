def sum(a, b):
    return a + b

def testSum():
    assert sum(1, 6) == 7
    assert sum(2, 6) == 8
    assert sum(1, 5) == 6


def hellow(name):
    return 'Привет' + name

def testHellow():
    assert hellow('Пока') == 'ПриветПока'
    assert hellow('привет') == 'Приветпривет'
    assert hellow('Пока') == 'ПриветПока'
    assert hellow('Пока') == 'ПриветПока'


