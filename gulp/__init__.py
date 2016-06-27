# -*- coding: utf-8 -*-

import logging
from functools import wraps
import time as t

__author__ = 'Cahyo Primawidodo'
__email__ = 'cahyo.p@gmail.com'
__version__ = '0.1.0'


def debug_lvl(lvl=logging.DEBUG):
    def enable(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            init = logging.getLogger().getEffectiveLevel()
            logging.getLogger().setLevel(lvl)
            y = f(*args, **kwargs)
            logging.getLogger().setLevel(init)
            return y
        return wrapper
    return enable


def time_profile(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_t = t.time()
        y = f(*args, **kwargs)
        end_t = t.time()
        print('{:5.3f} usec'.format(1000000 * (end_t-start_t)))
        return y
    return wrapper


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    print('running main')

    @debug_lvl()
    def x(*args, **kwargs):
        logging.debug('log x enabled')
        print('running x')

    @time_profile
    def y(*args, **kwargs):
        logging.debug('log y enabled')
        print('running y')

    x(1, 2, 3)
    y('abc')

