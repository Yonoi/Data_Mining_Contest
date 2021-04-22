'''
1. 分析事件传播速率和传播规模
作者: Mingjie
时间: 2021年4月4日
'''

import time
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

from datetime import datetime
from itertools import groupby

def calculate_diffusion_rate(filename, df):
    '''
    计算单位时间(1 hour)内原创和转发总数
    (按照重复记录条目的多少, 可以在引用该函数之前进行去重)
    '''
    child_nodes = list(df[u'MD5-mid'])
    times = list(df[u'发布日期'])

    times_second = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M")) for t in times]
    
    time_point = []
    number_of_tweets = []
    for index, group in groupby(sorted(times_second), 
        key=lambda x : (x - times_second[0]) // 3600):
        groups = list(group)
        time_point.append(groups[0])
        number_of_tweets.append(len(groups))

    # plt.hist(times_second, bins=bins)
    time_point = [datetime.fromtimestamp(t) for t in time_point]

    # 迭代求和
    sum_number_of_tweets = [sum(number_of_tweets[0:index])\
             for index in range(len(number_of_tweets))]

    ax1 = plt.subplot(1, 1, 1)
    ax2 = ax1.twinx()

    ax1.plot_date(time_point, number_of_tweets, linestyle='dotted', 
        marker='+', markersize=5, color='green', label="扩散速率")
    ax2.plot_date(time_point, sum_number_of_tweets, linestyle='solid', 
        marker='*', markersize=5, color='orange', label="扩散规模")

    plt.gcf().autofmt_xdate()
    fmt = mdates.DateFormatter("%Y/%m/%d %H:%M")
    plt.gca().xaxis.set_major_formatter(fmt)

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--扩散速率图'}")
    plt.xlabel('日期')  
    ax1.legend(loc="lower right")
    ax2.legend(loc="upper right")
    ax1.set_ylabel('扩散速率   (Tweets/h)')
    ax2.set_ylabel('扩散规模  (Tweets)')
    ax1.set_ylim(0, max(number_of_tweets))
    ax2.set_ylim(0, max(sum_number_of_tweets))
    plt.savefig(f"{'res/images/'+'扩散速率图--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()