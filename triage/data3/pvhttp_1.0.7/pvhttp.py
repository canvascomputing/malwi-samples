# -*- coding: utf-8 -*-

import time
import datetime
import logging
from collections import defaultdict


logger = logging.getLogger("pvhttp")


ALL_ENDPOINT_NAME = '*'
INTERVAL = 10


def catch_exc(func):
    import functools

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logger.error('exc occur.', exc_info=True)

    return func_wrapper


class MapleTimer(object):
    """
    按照一定的规则进行统计
    """

    app = None
    interval = None

    data_dict = None
    data_begin_time = None

    def __init__(self, app=None, config=None):
        self.reset_data()

        if app:
            self.init_app(app, config)

    def init_app(self, app, config=None):
        self.app = app
        config = config or dict()
        # 初始化数据
        self.interval = config.get('interval') or INTERVAL

        @app.before_request
        @catch_exc
        def prepare_stat(request):
            if not request.endpoint:
                return

            request.maple_timers = dict()
            request.maple_timers['begin_time'] = time.time()

        @app.after_request
        @catch_exc
        def send_stat(request, exc):
            if not hasattr(request, 'maple_timers'):
                return

            end_time = time.time()
            cost_time = end_time - request.maple_timers['begin_time']

            for it in (request.endpoint, ALL_ENDPOINT_NAME):
                self.data_dict[it]['count'] += 1
                self.data_dict[it]['total_time'] += cost_time
                self.data_dict[it]['upper_time'] = max(self.data_dict[it]['upper_time'], cost_time)

                if 'lower_time' not in self.data_dict[it]:
                    self.data_dict[it]['lower_time'] = cost_time
                else:
                    self.data_dict[it]['lower_time'] = min(self.data_dict[it]['lower_time'], cost_time)

            self.check_to_show_stat()

    def check_to_show_stat(self):
        now = datetime.datetime.now()

        if now - self.data_begin_time >= datetime.timedelta(seconds=self.interval):
            # 说明时间到了，可以打印了

            for k, v in self.data_dict.items():
                if self.data_dict[ALL_ENDPOINT_NAME]['count'] != 0:
                    v['count_percent'] = float(v['count']) / self.data_dict[ALL_ENDPOINT_NAME]['count']
                else:
                    v['count_percent'] = 0

                if self.data_dict[ALL_ENDPOINT_NAME]['total_time'] != 0:
                    v['total_time_percent'] = float(v['total_time']) / self.data_dict[ALL_ENDPOINT_NAME]['total_time']
                else:
                    v['total_time_percent'] = 0

            single_all_item = self.data_dict.pop(ALL_ENDPOINT_NAME)
            data_item_list = sorted(self.data_dict.items(), key=lambda x: x[1]['total_time'], reverse=True)
            data_item_list.insert(0, (ALL_ENDPOINT_NAME, single_all_item))

            self.show_stat(self.data_begin_time, now, data_item_list)

            self.reset_data()

    def reset_data(self):
        self.data_dict = defaultdict(lambda: defaultdict(int))
        self.data_begin_time = datetime.datetime.now()

    def show_stat(self, from_time, to_time, data_item_list):
        fmt = '%30s %20s %20s %12s %12s %12s %12s %12s'

        str_data_list = [
            fmt % ('endpoint',
                   'total_time_percent',
                   'count_percent',
                   'total_time',
                   'count',
                   'mean_time',
                   'upper_time',
                   'lower_time'
                   ),
        ]

        str_data_list.extend([
                                 fmt % (
                                     endpoint,
                                     '%.02f%%' % (data['total_time_percent'] * 100),
                                     '%.02f%%' % (data['count_percent'] * 100),
                                     '%.03f' % data['total_time'],
                                     data['count'],
                                     '%.03f' % (float(data['total_time']) / data['count']),
                                     '%.03f' % data['upper_time'],
                                     '%.03f' % data['lower_time'],
                                 )
                                 for endpoint, data in data_item_list
                                 ])

        logger.info('from %s to %s\n%s',
                    from_time,
                    to_time,
                    '\n'.join(str_data_list)
                    )
