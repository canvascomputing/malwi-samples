#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test the shorthand #abc hex expansion"""

import time
from colored.hex import HEX

def main():
    all_ok = True
    try:
        T_sta = time.perf_counter()
        for r in range(0,0xF):
            for g in range(0,0xF):
                for b in range(0,0xF):
                    short = '#%x%x%x' % (r,g,b)
                    long = '#%x%x%x%x%x%x' % (r,r,g,g,b,b)
                    all_ok = all_ok and HEX( long ) == HEX( short )
                print('.', end='')
            print('')

        dT = time.perf_counter() - T_sta
        print( 'Lookup time: %0.4f s => %0.4f s/lookup' % (dT, dT / (2*0xF*0xF*0xF) ) )
        print( 'pass' if all_ok else 'FAILED' )
    except Exception as e:
        print( 'Whopsie, something %s-ish went wrong: %s' % (e.__class__.__name__, e) )
        import traceback
        traceback.print_exc()
        all_ok = False

    return all_ok

if __name__ == "__main__":
    ok = main()
    exit( 0 if ok else 1 )
