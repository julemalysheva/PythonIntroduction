# нужно написать функцию расчета выражения комплексных чисел вместо eval
def calc_compl(data):
    res = eval(data) #eval работает, если на вход получает j вместо i
    # res = 'какой-то код'
    return res

import re
from collections import namedtuple
 
# Token = namedtuple('Token', ['type', 'value'])
 
# Определяем шаблоны
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' # шаблон для выражений типа 'foo = 1 + 1'
# EQ = r'(?P<EQ>=)'
'''NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
MULTIPLY = r'(?P<MULTIPLY>\*)'
DEVIDE = r'(?P<DEVIDE>\/)'
WS = r'(?P<WS>\s+)'
 
 
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
 
master_pat = re.compile('|'.join([NUM, PLUS, MINUS, MULTIPLY, DEVIDE, WS]))
 
for tok in generate_tokens(master_pat, '42+7-1/2'):
    print(tok)'''

a = input('a=')
b =  input('b=')
print(complex(a)+complex(b))
print(eval('2+4j+6-2j'))