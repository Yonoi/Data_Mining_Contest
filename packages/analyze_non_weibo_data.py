'''
1. 分析非微博数据中的媒体类型分布
2. 以及媒体名称排名
作者 : Mingjie
日期 : 4月9日
'''
import time
import matplotlib.pyplot as plt 

from collections import Counter, defaultdict

def media_type_distribution(filename, df):
    '''
    媒体类型分布
    '''
    media_type = df[u'媒体类型']
    count = Counter(media_type)

    x, y = [], []
    for key, value in sorted(count.items(), key=lambda x : x[1], reverse=False):
        x.append(key)
        y.append(value)

    b = plt.barh(x, y, color='tomato')
    for rect in b:
        w = rect.get_width()
        plt.text(w, rect.get_y() + rect.get_height() / 2, '%d' % int(w), ha='left', va='center', color='blue')

    plt.ylabel("媒体类型")
    plt.xlabel("分布数量")
    plt.title(f"{filename.replace('.csv', '').replace('data_non_weibo/', '') + '--媒体类型'}")
    plt.savefig(f"{'res/images/'+'媒体类型(非微博)--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()


def media_name_distribution(filename, df):
    '''
    媒体名称排名分布
    '''

    try:
        media_type = df[u'媒体名称']
    except KeyError:
        print(None)
        return
    count = Counter(media_type)

    x, y = [], []
    for key, value in sorted(count.items(), key=lambda x : x[1], reverse=True):
        x.append(key)
        y.append(value)


    # 画出排名前十的媒体
    x, y = x[:10], y[:10]

    b = plt.barh(x, y, color='seagreen')
    for rect in b:
        w = rect.get_width()
        plt.text(w, rect.get_y() + rect.get_height() / 2, '%d' % int(w), ha='left', va='center', color='blue')

    plt.ylabel("媒体名称")
    plt.xlabel("分布数量")
    plt.title(f"{filename.replace('.csv', '').replace('data_non_weibo/', '') + '--媒体名称'}")
    plt.savefig(f"{'res/images/'+'媒体名称(非微博)--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()