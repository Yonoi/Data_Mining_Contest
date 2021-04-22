'''
1. 分析用户特征
2. 性别分布
3. 认证类型
4. 粉丝数量区间分布
作者 : Mingjie
日期 : 4月8日

'''
import time
import matplotlib.pyplot as plt 

from collections import Counter, defaultdict

def gender_distribution(filename, df):
    '''
    性别分布
    '''
    gender = df[u'性别']
    count = Counter(gender)
    
    labels = [u'男', u'女']
    x = [count[each] for each in labels]

    explode = [0] * len(x)
    explode[-1] = 0.02

    explode = tuple(explode)

    patches, l_text, p_text =  plt.pie(x, labels=labels, explode=explode, labeldistance=1.1,
        startangle=0, autopct='%2.2f%%', shadow=False, pctdistance=0.8)
    plt.pie(x, radius=0.6, colors='w')
    for t in l_text:
        t.set_size = 30

    for t in p_text:
        t.set_size = 20

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--性别分布'}")
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))  
    plt.savefig(f"{'res/images/'+'性别分布--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()

def authentication_type(filename, df):
    '''
    认证类型分布
    '''
    auth = df[u'认证类型']
    count = Counter(auth)

    x, labels = [], []
    for key, value in sorted(count.items(), key=lambda x : x[1], reverse=True):
        labels.append(key)
        x.append(value)

    explode = [0] * len(x)
    if len(explode) >= 3:
        explode[-4 : ] = [0.02, 0.05, 0.08, 0.1]
    else:
        explode[-1] = 0.1 
    explode = tuple(explode)

    patches, l_text, p_text =  plt.pie(x, labels=labels, explode=explode, labeldistance=1.1,
        startangle=0, autopct='%2.2f%%', shadow=False, pctdistance=0.8)

    plt.pie(x, radius=0.6, colors='w')
    for t in l_text:
        t.set_size = 30

    for t in p_text:
        t.set_size = 20

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--认证类型'}")
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))  
    plt.savefig(f"{'res/images/'+'认证类型--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()

def number_of_fans_distributions(filename, df):
    '''
    粉丝数量区间分布
    '''
    number_of_fans = df[u'粉丝数']

    x = ['0-49', '50-199', '200-499', '500-799', '800-1399', '1400-1999', 
        '2000-2999', '3000-4999', '5000-10000', u'10000以上']
    section = [[0], list(range(1, 4)), list(range(4, 10)), list(range(10, 16)),
                list(range(16, 28)), list(range(28, 40)), list(range(40, 60)),
                list(range(60, 100)), list(range(100, 200))]

    d = defaultdict(int)
    for each in x:
        d[each] = 0

    for fans in number_of_fans:
        index = fans // 50
        for i, sec in enumerate(section):
            if index in sec:
                d[x[i]] += 1
                break
        else:
            d[x[-1]] += 1
    
    height = list(d.values())

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--粉丝区间分布'}")
    plt.bar(x, height, color='orange', label=u'该区间总数')
    plt.xlabel("粉丝数区间")
    plt.gcf().autofmt_xdate()

    for a, b in zip(x, height):
        plt.text(a, b + 0.05, b, ha='center', va='bottom', color='blue')
    plt.legend()
    plt.savefig(f"{'res/images/'+'粉丝区间分布--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()