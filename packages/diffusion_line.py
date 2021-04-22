'''
1. 分别观察转发和原创两种类型微博数量随着时间变化的曲线
作者: Mingjie
时间: 2021年4月4日
'''

import time
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from datetime import datetime
from itertools import groupby

def count_tweets(times):
    '''
    统计一个小时内的微博数
    返回积分的时间点以及微博数
    '''
    times_second = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M")) for t in times]
    time_point = []
    number_of_tweets = []
    for index, group in groupby(sorted(times_second), 
        key=lambda x : (x - times_second[0]) // 3600):
        groups = list(group)
        time_point.append(groups[0])
        number_of_tweets.append(len(groups))
    
    return time_point, number_of_tweets


def analyze_diffusion_line(filename, df):
    '''
    分别观察转发和原创两种类型微博数量随着时间变化的曲线
    '''
    event_type = list(df[u'原创/转发'])
    times = list(df[u'发布日期'])

    original_time = [] 
    forward_time = []

    for index, e_type in enumerate(event_type):
        if e_type == u'原创':
            original_time.append(times[index])
        else:
            forward_time.append(times[index])

    time_point, original_number_of_tweets = count_tweets(original_time)
    original_time_point = [datetime.fromtimestamp(t) for t in time_point]

    time_point, forward_number_of_tweets = count_tweets(forward_time)
    forward_time_point = [datetime.fromtimestamp(t) for t in time_point]

    # 画事件规模上升曲线
    original_number_of_tweets = [sum(original_number_of_tweets[0:index])\
             for index in range(len(original_number_of_tweets))]

    forward_number_of_tweets = [sum(forward_number_of_tweets[0:index])\
             for index in range(len(forward_number_of_tweets))]

    plt.plot_date(original_time_point, original_number_of_tweets, linestyle='solid', 
        marker='+', color='orange', label="原创")
    plt.plot_date(forward_time_point, forward_number_of_tweets, linestyle='solid', 
        marker='*', color='blue', label="转发")

    plt.gcf().autofmt_xdate()
    fmt = mdates.DateFormatter("%Y/%m/%d %H:%M")
    plt.gca().xaxis.set_major_formatter(fmt)

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--事件传播特征'}")
    plt.xlabel('Date')  
    plt.ylabel('总微博量')
    plt.legend(loc="upper left")
    plt.savefig(f"{'res/images/'+'事件传播线--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()
