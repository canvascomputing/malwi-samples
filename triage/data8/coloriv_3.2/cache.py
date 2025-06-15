"""A Cache manegement util."""

import json
import os
import pickle
from eic_utils.base import colorful_str

__all__ = ['Cache']

__read = lambda f: f.read()
__write_str = lambda data, f: f.write('{}'.format(data))
__write_bin = lambda data, f: f.write(data)

FILE_OPS = {
    'str': {'suffix': 'txt', 'r': 'r', 'w': 'w',
            'load': __read, 'dump': __write_str}, 
    'pkl': {'suffix': 'pkl', 'r': 'rb', 'w': 'wb',
            'load': pickle.load, 'dump': pickle.dump},
    'json': {'suffix': 'json', 'r': 'r', 'w': 'w',
             'load': json.load, 'dump': json.dump},
    'bin': {'suffix': 'bin', 'r': 'rb', 'w': 'wb',
            'load': __read, 'dump': __write_bin},
}


class Cache(object):
    """Stores files into different formats."""

    def __init__(self, path):
        """Stores caches in 'path'."""

        self.path = path
        self.file_op = FILE_OPS
        if not os.path.isdir(path):
            os.makedirs(path)

    def items(self):
        """A list of all items stored."""

        return sorted(os.listdir(self.path))

    def remove(self, name):
        """Deletes the target."""

        path = os.path.join(self.path, name)
        if os.path.isfile(path):
            os.remove(path)
            return True
        return False

    def dump(self, data, name, file_type='pkl'):
        """Saves data into name.

        Args:
            data: Data to save.
            name: Name of output file.
            file_type: Type of the output file, must be one of 
                       ['str', 'pkl', 'json', 'bin'], default 'pkl'.
        """

        assert file_type in self.file_op.keys(), colorful_str.err(
            'key error: (#y){}(#) not found in (#y){}(#)'.format(
                file_type, list(self.file_op.keys())))

        path = os.path.join(self.path, name)
        file_op = self.file_op[file_type]
        with open(path, file_op['w']) as f:
            file_op['dump'](data, f)

    def load(self, name, file_type='pkl'):
        """Lodas data from name.

        Args:
            name: Name of output file.
            file_type: Type of the output file, must be one of 
                       ['str', 'pkl', 'json', 'bin'], default 'pkl'.
        """

        assert file_type in self.file_op.keys(), colorful_str.err(
            'key error: (#y){}(#) not found in (#y){}(#)'.format(
                file_type, list(self.file_op.keys())))

        path = os.path.join(self.path, name)
        file_op = self.file_op[file_type]
        with open(path, file_op['r']) as f:
            return file_op['load'](f)
