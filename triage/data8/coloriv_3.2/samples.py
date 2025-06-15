import eic_utils
from eic_utils import base
from eic_utils.base import colorful_str
from eic_utils.base import procedure
from eic_utils.cache import Cache
from eic_utils.database import Database
import numpy as np

def procedure_test():
    """Test class 'Procedure'."""

    with procedure('hi') as p:
        x = 123 + 123
        p.show_time('x has be calculated.', x)
        p.add_log('x =', x)
        y = x + 34
        p.add_log('y =', y)

def colorful_str_test():
    "Test ColorfulStr."

    print(colorful_str('(#r)this is a red message.(#)',
                       'this is a normal message.',
                       '(#b)this is a blue value {}(#).'.format(2),
                       '(#g)this is a green dict {}.'.format({1:2})))
    print(colorful_str.log('(#r)this is a red message.(#)',
                           'this is a normal message.',
                           '(#b)this is a blue value {}(#).'.format(2),
                           '(#g)this is a green dict {}.'.format({1:2})))
    print(colorful_str.suc('(#r)this is a red message.(#)',
                           'this is a normal message.',
                           '(#b)this is a blue value {}(#).'.format(2),
                           '(#g)this is a green dict {}.'.format({1:2})))
    print(colorful_str.err('(#r)this is a red message.(#)',
                           'this is a normal message.',
                           '(#b)this is a blue value {}(#).'.format(2),
                           '(#g)this is a green dict {}.'.format({1:2})))
    print(colorful_str.wrn('(#r)this is a red message.(#)',
                           'this is a normal message.',
                           '(#b)this is a blue value {}(#).'.format(2),
                           '(#g)this is a green dict {}.'.format({1:2})))
    print(colorful_str.dict({'a': 's', 'b': 's'}))


def test():
    procedure_test()
    colorful_str_test()
    print(base.get_cur_time())
    print(base.get_cur_time(nano_second=True))

    cache = Cache('/tmp')
    cache.dump('hi', 'a.pkl')
    print(cache.load('a.pkl', file_type='pkl'))
    
if __name__ == '__main__':
    test()
