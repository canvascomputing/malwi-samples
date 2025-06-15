#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test the nearest matching hex color lookup"""

import time
from random import randint
from colored import fg, bg, attr
from colored.hex import HEX, _xterm_colors

def compare_with_expected( in_hex, expected ):
    nearest = HEX( in_hex )
    # Look up the matched hex value (e.g. xterm colors 10 and 46 are
    # the same hex value)
    match = _xterm_colors[nearest] == _xterm_colors[expected]

    e_str = '%s%s##%s' % (fg( expected ), bg( expected ), attr('reset'))
    n_str = '%s%s##%s' % (fg( nearest ), bg( nearest ), attr('reset'))
    print( "%s: %s => %s = %s" % ( 'pass' if match else 'FAIL', in_hex, n_str, e_str) )

    return match

def main():
    print( '            Nearest   Expected' )
    test_set = {
        '1':  ('#7f0000', '#800000', '#810000'),
        '2':  ('#007f00', '#008000', '#008100'),
        '4':  ('#00007f', '#000080', '#000081'),
        '10': ('#00fe00', '#00ff00', '#01ff00'),
    }

    all_ok = True
    for expected, hexes in test_set.items():
        for hex in hexes:
            ok = compare_with_expected( hex, expected )
            all_ok = all_ok and ok

    try:
        T_sta = time.perf_counter()
        print( '-'*78 )
        for y in range(0,0xF):
            r_row = ''
            g_row = ''
            b_row = ''
            i_row = ''
            for x in range(0,0xF):
                c = x + y*0xF
                hex = '#%02x0000' % (c,)
                r_row += '%s%s#' % (fg(hex),bg(hex))
                hex = '#00%02x00' % (c,)
                g_row += '%s%s#' % (fg(hex),bg(hex))
                hex = '#0000%02x' % (c,)
                b_row += '%s%s#' % (fg(hex),bg(hex))
                hex = '#'+('%02x' % (c,))*3
                i_row += '%s%s#' % (fg(hex),bg(hex))
            print( '%s%s %s%s %s%s %s%s' % (r_row,attr('reset'), g_row,attr('reset'), b_row,attr('reset'), i_row,attr('reset')) )
        dT = time.perf_counter() - T_sta
        print( 'Lookup time: %0.4f s => %0.4f s/lookup' % (dT, dT / (2*4*0xFF) ) )
        print( '-'*78 )
    except Exception as e:
        print( 'Whopsie, something %s-ish went wrong: %s' % (e.__class__.__name__, e) )
        import traceback
        traceback.print_exc()
        all_ok = False

    # This is just for fun, almost... let's call it a
    # "non-deterministic check that it doesn't throw any exceptions"
    try:
        T_sta = time.perf_counter()
        from random import randint
        for y in range(0,20):
            for x in range(0,30):
                rnd = randint(0,0xffffff)
                hex = '#%06x' % (rnd,)
                hexinv = '#%06x' % (0xffffff-rnd,)
                print( '%s%s::' % (fg(hexinv),bg(hex)), end='')
            print( attr('reset') )
        dT = time.perf_counter() - T_sta
        print( 'Lookup time: %0.4f s => %0.4f s/lookup' % (dT, dT / (2*30*20) ) )
    except Exception as e:
        print( 'Whopsie, something %s-ish went wrong: ' % (e.__class__.__name__, e) )
        all_ok = False

    return all_ok

if __name__ == "__main__":
    ok = main()
    exit( 0 if ok else 1 )
