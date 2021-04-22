'''
1. 读取csv文件, 分析微博数据的事件总数, 抓取时间
2. 重复微博个数
3. 构建事件扩散网络, 保存res/*.adjlist文件
作者: Mingjie
时间: 2021年4月1日
'''
import os
import time
import collections

import numpy as np
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

from itertools import chain
from datetime import datetime
from collections import Counter, defaultdict


def number_of_repeat_tweets(df):
    '''
    统计重复推文的数量
    返回重复推文index
    '''
    print(f"没有去重的记录条数 : {len(df)}")
    repeat_tweets = [(item, count) for item, count in \
        collections.Counter(df[u'MD5-mid']).items() if count > 1]
    print(f"去重之后的记录条数 : {len(df) - sum(map(lambda x : x[1], repeat_tweets)) + len(repeat_tweets)}")
    return repeat_tweets

def get_index(mid_list, element):
    '''
    delete_repeat_tweets的子函数
    '''
    index = [0]
    while len(index) <= element[1]:
        index.append(mid_list.index(element[0], index[-1]))
    return index

def delete_repeat_tweets(df, repeat_tweets):
    '''
    在表格中删除重复推文
    返回新的df
    '''
    child_nodes = list(df[u'MD5-mid'])
    for element in repeat_tweets:
        # 得到重复信息
        index = get_index(child_nodes, element)
        index = index[:-2]
        df.drop(index, axis=0)
    return df

def collection_time(df):
    '''
    采集信息时长
    直接打印
    '''
    times = list(df[u'发布日期'])
    times_datetime = [datetime.strptime(t, "%Y/%m/%d %H:%M") for t in times]
    diff_time = times_datetime[-1] - times_datetime[0]
    print(f"采集时长 (days/hours/mintues) : {diff_time.days}/{diff_time.seconds // 3600}/{diff_time.seconds % 3600 // 60}")

def non_weibo_data_analysis(df):
    '''
    对非微博数据进行简要分析
    包括采集数目, 参与媒体数目
    '''
    try:
        media_type = df[u'媒体名称']
    except KeyError:
        print(None)
        return
    count = Counter(media_type)
    print(f"采集条目数: {len(df)}")
    print(f"媒体参与数目 :　{len(count)}")

def csv2adjlist(filename, df, RESULT_DIR):
    '''
    构建基于事件传播的网络图
    '''
    child_nodes = list(df[u'MD5-mid'])
    parent_nodes = list(df[u'MD5-父微博ID'])
    times = list(df[u'发布日期'])

    G = nx.DiGraph()
    for index, edge in enumerate(zip(child_nodes, parent_nodes)):
        v, u = edge
        if str(u) == 'nan':
            G.add_node(v)
        else:
            G.add_edge(u, v, time=times[index])
    
    print(f"nodes : {G.number_of_nodes()}, edges : {G.number_of_edges()}")
    nx.write_adjlist(G, RESULT_DIR + 'adjlist/'+filename.replace('.csv', '.adjlist'))
    print("事件扩散网络数据已经保存!!")
