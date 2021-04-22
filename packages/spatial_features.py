'''
1. 事件的空间特征
2. 国内外分布
3. 国内各省市分布
作者 : Mingjie
日期 : 4月8日
'''
import time
import pandas as pd
import matplotlib.pyplot as plt 
from collections import Counter, defaultdict

def event_spatial_distribution_in_the_world(filename, df):
    '''
    事件发生所在地在国内外的分布情况
    '''
    locations = df[u'地域']

    count = Counter(locations)
    if u'海外' in count.keys():
        national_names = [u"海外", u"国内"]
        x = [count[u'海外'], sum(count.values()) - count[u'海外']]
    else:
        national_names = [u'国内']
        x = [sum(count.values())]
    labels = national_names
    
    explode = [0] * len(x)
    explode[-1] = 0.1

    explode = tuple(explode)

    patches, l_text, p_text =  plt.pie(x, labels=labels, explode=explode, labeldistance=1.1,
        startangle=0, autopct='%2.2f%%', shadow=False)
    for t in l_text:
        t.set_size = 30

    for t in p_text:
        t.set_size = 20

    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--国内外分布'}")
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))  
    plt.savefig(f"{'res/images/'+'国内外分布--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()

def event_spatial_distribution_in_the_china(filename, df):
    '''
    事件发生所在地, 在国内各省市的分布情况
    区分转发和原创
    '''

    locations = df[u'地域']
    event_type = df[u'原创/转发']

    new_df = pd.DataFrame({u'地域':locations, u'原创/转发':event_type})
    group = new_df.groupby(u'地域')
    
    location_names = ['重庆', '辽宁', '河北', '北京', '广东', '青海', '黑龙江',
                      '江苏', '山东', '广西', '河南', '上海', '陕西', '四川', 
                      '湖南', '湖北', '吉林', '云南', '海南', '浙江', '江西',
                      '福建', '安徽', '甘肃', '内蒙古', '山西', '新疆', '西藏', 
                      '贵州', '天津', '香港', '台湾', '宁夏', '澳门']

    d = defaultdict(list)
    for key in location_names:
        d[key] = [0, 0]

    for province in group:
        if province[0] == u'海外':
            continue
        count = Counter(province[1][u'原创/转发'])
        d[province[0]] = [count[u'原创'], count[u'转发']]

    x = []
    orignal_height = []
    forward_height = []
    for key, value in sorted(d.items(), key=lambda x : sum(x[1]), reverse=True):
        x.append(key)
        orignal_height.append(value[0])
        forward_height.append(value[1])
    
    plt.title(f"{filename.replace('.csv', '').replace('data/', '') + '--各省市分布'}")
    plt.bar(x, orignal_height, color='blue', label=u'原创')
    plt.bar(x, forward_height, color='orange', label=u'转发', bottom=orignal_height)
    plt.ylabel("数量")
    plt.gcf().autofmt_xdate()

    for a, b, c in zip(x, orignal_height, forward_height):
        if b == 0:
            plt.text(a, b + c + 2, b + c, ha='center', va='bottom', color='black')
            continue
        elif c == 0:
            
            continue
        plt.text(a, b + c + 2, b + c, ha='center', va='bottom', color='black')
        plt.text(a, b + 0.05, b, ha='center', va='bottom', color='blue')

    plt.legend()
    plt.savefig(f"{'res/images/'+'各省市分布--' + filename.replace('.csv', '').replace('data/', '')}", dpi=800)
    plt.show()
    