'''
1. 分析该事件的敏感性
2. 分析用户对于该事件的情感倾向
3. 分析用户情绪在该事件中随时间变化的曲线特征
作者 : Mingjie
时间 : 4月8日 
'''
import time
import matplotlib.dates as mdates
import matplotlib.pyplot as plt 

from datetime import datetime
from itertools import groupby
from collections import Counter, defaultdict

def analyze_novel(filename, df):
    '''
    分析事件新奇性(这里用敏感性替代)
    '''
    novel = df[u'信息属性']
    count = Counter(novel)

    x, labels = [], []
    for key, value in sorted(count.items(), key=lambda x : x[1], reverse=True):
        labels.append(key)
        x.append(value)
    
    explode = [0] * len(x)
    if len(explode) == 3:
        explode[-2 : ] = [0.05, 0.1]
    else:
        explode[-1] = 0.1 
    explode = tuple(explode)

    patches, l_text, p_text =  plt.pie(x, labels=labels, explode=explode, labeldistance=1.1,
        startangle=0, autopct='%2.2f%%', shadow=False)

    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--信息敏感性'}")
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))  
    plt.savefig(f"{'res/images/'+'信息敏感性--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()


def analyze_emotion(filename, df):
    '''
    分析用户对该事件的情绪
    '''
    emotion = df[u'微博情绪']
    count = Counter(emotion)

    x, labels = [], []
    for key, value in sorted(count.items(), key=lambda x : x[1], reverse=True):
        labels.append(key)
        x.append(value)

    # 至少三种情感, 才区分
    explode = [0] * len(x)
    if len(explode) >= 3:
        explode[-3 : ] = [0.05, 0.1, 0.2]
    explode = tuple(explode)
    
    patches, l_text, p_text =  plt.pie(x, labels=labels, explode=explode, labeldistance=1.1,
        startangle=0, autopct='%2.2f%%', shadow=False)
    for t in l_text:
        t.set_size = 30

    for t in p_text:
        t.set_size = 20

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--情感分析'}")
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))  
    plt.savefig(f"{'res/images/'+'情感分析--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()

def count_emotion(times):
    times_second = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M")) for t in times]
    time_point = []
    number_of_tweets = []
    for index, group in groupby(sorted(times_second), 
        key=lambda x : (x - times_second[0]) // 3600):
        groups = list(group)
        time_point.append(groups[0])
        number_of_tweets.append(len(groups))
    
    return time_point, number_of_tweets

def emotion_evolution(filename, df):
    '''
    分析用户对该事件的随时间变化的情感曲线
    '''
    emotion_type = list(df[u'微博情绪'])
    times = list(df[u'发布日期'])

    emotion_type_time = defaultdict(list)
    for e_type in set(emotion_type):
        emotion_type_time[e_type] = []
    
    for index, e_type in enumerate(emotion_type):
            emotion_type_time[e_type].append(times[index])

    for e_type in set(emotion_type):
        time_point, number_of_emotion = count_emotion(emotion_type_time[e_type])
        time_point = [datetime.fromtimestamp(t) for t in time_point]
        plt.plot_date(time_point, number_of_emotion, label=e_type, linestyle='solid', markersize=3)

    plt.gcf().autofmt_xdate()
    fmt = mdates.DateFormatter("%Y/%m/%d %H:%M")
    plt.gca().xaxis.set_major_formatter(fmt)

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--情感变化'}")
    plt.xlabel('日期')  
    plt.ylabel('情感总数')
    plt.legend(loc="upper left")
    plt.savefig(f"{'res/images/'+'情感变化--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()
