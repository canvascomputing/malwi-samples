import datetime, time
import calendar

now = datetime.datetime.now()


def get_time(year=now.year,
             month=now.month,
             day=now.day,
             hour=now.hour,
             minute=now.minute,
             second=now.second,
             week=-1,
             last_day_of_month=False,
             type="time",
             detail=True):
    """

    :param year: 年 (默认今年)
    :param month: 月 (默认当月)
    :param day: 天 (默认今天)
    :param hour: 时 (默认当前时间)
    :param minute: 分 (默认当前时间)
    :param second: 秒 (默认当前时间)
    :param week: 星期x (默认-1,如果不等于-1,则day参数无效)
    :param last_day_of_month: 每个月的最后一天 (默认False)
    :param type: 输出类型 (time / str)
    :param detail: 是否输出时分秒? (默认输出时分秒)
    :return: 时间 
    """

    if week != -1:
        weekday = datetime.datetime(year, month, day, hour, minute, second)

        one_day = datetime.timedelta(days=1)
        while weekday.weekday() != 0:
            weekday -= one_day

        ret = weekday + datetime.timedelta(days=week - 1)

    else:

        if last_day_of_month:  # 每个月的最后一天
            day = calendar.monthrange(year, month)[1]

        if not detail:
            date = datetime.date(year, month, day)
        else:
            date = datetime.datetime(year, month, day, hour, minute, second)

        ret = date if type == "time" else str(date)

    return ret


def get_timestamp(detail=True):
    """
    获取当前时间戳 
    :param detail: True输出完整的时间戳/ False输出前10位(小数点之前)
    :return: 时间戳 
    """
    if detail:
        ret = time.time()
    else:
        ret = int(time.time())
    return ret


def timestamp_to_str(timestamp, strformat):
    """
    时间戳转字符串
    :param timestamp: 时间戳 
    :param strformat: 转换格式 (%Y-%m-%d %H:%M:%S)
    :return: 时间字符串 
    """
    ret = time.strftime(strformat, time.localtime(timestamp)) 

    return ret


def str_to_timestamp(timestr, strformat):
    """
    字符串转时间戳 
    :param timestr: 时间字符串 
    :param strformat: 转换格式 (%Y-%m-%d %H:%M:%S) 
    :return: 时间戳 (前10位)
    """
    ret = int(time.mktime(time.strptime(timestr, strformat)))

    return ret