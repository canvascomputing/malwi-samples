"""Basic tools.

Includes:
    MultipleReplace: Replaces a series of keys to values.
    ColorfulStr: Makes logs coloful. (use its instance)
    colorful_str: an instance of ColorfulStr.
    Procedure: Timer for a blocks of codes.
    procedure: The same as Procedure.
"""
import datetime
import re
import time


class MultipleReplace:
    """Replaces a series of keys to values."""

    def __init__(self, rep_dict):
        """Initialize the pattern.

        Args:
            rep_dict: A dict, in which all keys and values must be str.
        """
        self.rep_dict = rep_dict.copy()
        self.pattern = re.compile(
            "|".join([re.escape(k) for k in self.rep_dict.keys()]), re.M)

    def replace(self, string):
        """Replaces the given str according to the pattern."""
        return self.pattern.sub(lambda x: self.rep_dict[x.group(0)], string)


class ColorfulStr:
    """Makes logs colorful.

    Usage:
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

    Valid color codes:
        (#black):black
        (#r), (#red): red
        (#g), (#green): green
        (#y), (#yellow): yellow
        (#b), (#blue): blue
        (#magenta): magenta
        (#cyan): cyan
        (#w), (#white): white
        (#): default
    """

    def __init__(self):
        self.colors = {
            'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
            'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
            'b': 34, 'r': 31, 'g': 32, 'y': 33, 'w': 37,
        }
        self.done = '(#g)done(#)'
        self.prefix = '\033[1;{}m'
        self.suffix = '\033[1;0m'
        table = {'(#{})'.format(k): self.prefix.format(v)
                 for k, v in self.colors.items()}
        table.update({'(#)': self.suffix})
        self.multiple_replace = MultipleReplace(table)

    def __call__(self, *args):
        """Transforms (#color) to codes and returns log strings.

        Usages:
            print(colorful_str('(#r)this is a red message.(#)',
                               'this is a normal message.',
                               '(#b)this is a blue value {}(#).'.format(2),
                               '(#g)this is a green dict {}.'.format({1:2})))

        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """
        output = (self.suffix+' ').join(map('{}'.format, args)) + self.suffix
        output = self.multiple_replace.replace(output)
        return output

    def err(self, *args):
        """Error message.

        Usages:
            print(colorful_str.err('(#r)this is a red message.(#)',
                                   'this is a normal message.',
                                   '(#b)this is a blue value {}(#).'.format(2),
                                   '(#g)this is a green dict {}.'.format({1:2})))

        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """
        return self('(#r)[ERR](#)', *args)

    def log(self, *args):
        """Log message.
        Usages:
            print(colorful_str.log('(#r)this is a red message.(#)',
                                   'this is a normal message.',
                                   '(#b)this is a blue value {}(#).'.format(2),
                                   '(#g)this is a green dict {}.'.format({1:2})))
        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """

        return self('(#b)[LOG](#)', *args)

    def wrn(self, *args):
        """Warning message.

        Usages:
            print(colorful_str.wrn('(#r)this is a red message.(#)',
                                   'this is a normal message.',
                                   '(#b)this is a blue value {}(#).'.format(2),
                                   '(#g)this is a green dict {}.'.format({1:2})))

        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """
        return self('(#y)[WRN](#)', *args)

    def suc(self, *args):
        """Successful message.

        Usage:
            print(colorful_str.suc('(#r)this is a red message.(#)',
                                   'this is a normal message.',
                                   '(#b)this is a blue value {}(#).'.format(2),
                                   '(#g)this is a green dict {}.'.format({1:2})))

        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """
        return self('(#g)[SUC](#)', *args)

    def dict(self, data):
        """Makes values of a dict yellow."""

        assert isinstance(data, dict), 'Data must be a dict.'
        output = ', '.join(['{}: (#y){}(#)'.format(k, v)
                            for k, v in sorted(data.items())])
        return self('{{{}}}'.format(output))

    def color(self, *args, color='#g'):
        if color[0] == '#':
            color = '({})'.format(color)
        return ['{}{}(#)'.format(color, x) for x in args]

class ColorfulPrint(ColorfulStr):

    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        """Transforms (#color) to codes and prints log strings.

        Usages:
            print(colorful_str('(#r)this is a red message.(#)',
                               'this is a normal message.',
                               '(#b)this is a blue value {}(#).'.format(2),
                               '(#g)this is a green dict {}.'.format({1:2})))

        Valid color codes:
            (#black):black
            (#r), (#red): red
            (#g), (#green): green
            (#y), (#yellow): yellow
            (#b), (#blue): blue
            (#magenta): magenta
            (#cyan): cyan
            (#w), (#white): white
            (#): default
        """
        output = (self.suffix+' ').join(map('{}'.format, args)) + self.suffix
        output = self.multiple_replace.replace(output)
        print(output)


colorful_str = ColorfulStr()
colorful_print = ColorfulPrint()


class Procedure:
    """Timer for a blocks of codes.

    Usage:
        with Procedure('hi') as p:
            x = 123 + 123
            p.show_time('x has be calculated.', x)
            p.add_log('x =', x)
            y = x + 34
            p.add_log('y =', y)
    """

    def __init__(self, msg, new_line=False):
        self.logs = [msg]
        self.new_line = new_line
        self.time = time.time()

    def __print(self, colorful, end='\n', logs=None):
        if logs is None:
            logs = self.logs
        print(colorful(*logs), end=end)

    def __enter__(self):
        self.__print(colorful_str.log, '\n' if self.new_line else '\r')
        return self

    def __exit__(self, _, __, traceback):
        delta_time = datetime.timedelta(seconds=time.time()-self.time)
        self.add_log(colorful_str.done, 'time: (#b){}(#)'.format(delta_time))
        self.__print(
            colorful_str.suc if traceback is None else colorful_str.err)

    def add_log(self, *args):
        """Add logs to final print when exiting."""
        self.logs += args

    def show_time(self, *logs):
        """Display logs and delta time."""
        self.__print(colorful_str.log, logs=logs)

procedure = Procedure


def get_cur_time(nano_second=False):
    """Gets time in format year/month/day hour:mintes:seconds nanoseconds."""

    res = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    if nano_second:
        res = res + ' {:09d}'.format(round(time.time() % 1 * 1e9))
    return res


def __procedure_test():
    """Test class 'Procedure'."""

    with Procedure('hi') as p:
        x = 123 + 123
        p.show_time('x has be calculated.', x)
        p.add_log('x =', x)
        y = x + 34
        p.add_log('y =', y)

def __colorful_str_test():
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


def __test():
    __procedure_test()
    __colorful_str_test()
    print(get_cur_time())
    print(get_cur_time(nano_second=True))
    colorful_print('(#y)123', get_cur_time())
    
    # usage of new updates
    colorful_print('this is a test, x = {}, y = {}, z = {}'.format(
        *colorful_print.color(1, 2, 3, color='(#b)')))

if __name__ == '__main__':
    __test()
