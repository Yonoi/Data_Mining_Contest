import os
import time

import pandas as pd 
import matplotlib as mpl

from packages.create_network import *
from packages.analyze_network import *
from packages.diffusion_rate import *
from packages.diffusion_line import *
from packages.analyze_novel_and_emotion import *
from packages.spatial_features import *
from packages.user_features import *
from packages.analyze_non_weibo_data import *

# 设置字体
mpl.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei Mono']

"""
# 微博数据文件名称以及对应序号
 0 福建泉州一酒店发生坍塌事故.csv
 1 第33届中国电影金鸡奖开幕式.csv
 2 腾讯状告老干妈事件-2.csv
 3 重庆尾号888888手机号法拍85万.csv
 4 广州落户门槛降低.csv
 5 凉山木里县境内发生森林火灾.csv
 6 安徽推行机动车检验标志电子化.csv
 7 腾讯状告老干妈事件-1.csv
 8 丁真回应意外走红.csv
 9 河北一幼儿园食堂现发臭肉馅.csv
10 上海名媛群争议.csv
11 2020年广州国际车展举办.csv
12 合安高铁进入试运行.csv
13 海南进入生活垃圾全焚烧时代.csv
14 上海野生动物园熊伤人致1人死亡.csv
15 唐山大地震44周年.csv
16 《海南自由贸易港建设总体方案》印发.csv
17 长征八号首飞成功.csv
18 温岭大溪一油罐车发生爆炸.csv
19 2020世界5G大会开幕.csv
20 深圳推行强制休假制度.csv
21 男子被浴室玻璃门割伤手.csv
22 数字人民币正在雄安新区等地试点测试.csv
23 重庆警方通报城管追打女商贩被砍伤.csv
24 安徽歙县内涝严重道路无法通行.csv
"""

DATA_DIR = 'data/'
# DATA_DIR = 'data_non_weibo/' # 非微博数据
RESULT_DIR = 'res/'

def get_filename(path):
    filenames = os.listdir(path)

    if filenames is None:
        print(f"The directory of {path} is empty!")
    else:
        print("Filenames obtained successfully!")
    return filenames

def main():
    start_time = time.time()
    filenames = get_filename(DATA_DIR)

    # True 只测试一个文件, 文件编号为上述注释部分
    TEST = True

    if TEST == True:
        '''
        以下每个函数都可独立运行, 运行时, 只需要将其他函数注释即可.
        '''
        # 可以修改为想要测试的文件, 1, 2, 3...
        # 例子 : 合安高铁进入试运行.csv
        file_index = 12 
        filename = filenames[file_index]
        
        print(f"文件名 : {filename}")

        df = pd.read_csv(DATA_DIR + filename, encoding='gb18030')

        # 数据集微博总数, 重复总数
        repeat_tweets = number_of_repeat_tweets(df)

        # 删除重复的推文(后续有些函数如需使用删除微博分析, 可以将该语句注释去除, 但是运行较慢)
        # df = delete_repeat_tweets(df, repeat_tweets)

        # 文件中数据的采集时间
        # collection_time(df)

        # 分析原始非微博数据, 此时需要修改DATA_DIR = 'data_non_weibo/'
        # non_weibo_data_analysis(df)
        
        # 分析非微博数据中媒体类型分布
        # media_type_distribution(filename, df)
        
        # 分析非微博数据中媒体名称排名
        # media_name_distribution(filename, df)

        # 利用原始数据构造事件扩散网络(是否删除重复推文对构造网络无影响)
        # csv2adjlist(filename, df, RESULT_DIR)

        # 对于图分析, 需要临时修改一下路径, 只有该文件需要修改路径,
        # filename = RESULT_DIR + 'adjlist/' + filename.replace('.csv', '.adjlist')
        # analyze_graph(filename)
        # filename = filenames[file_index]

        # 分析事件传播速率和传播规模曲线
        # calculate_diffusion_rate(filename, df)

        # 分别观察转发和原创两种类型微博数量随着时间变化的曲线
        # analyze_diffusion_line(filename, df)

        # 分析事件新奇性
        # analyze_novel(filename, df)

        # 分析用户对事件的情绪
        # analyze_emotion(filename, df)

        # 分析用户的情绪演进
        # emotion_evolution(filename, df)
        
        # 国内外分布
        # event_spatial_distribution_in_the_world(filename, df)

        # 国内各省市分布 分原创和转发
        # event_spatial_distribution_in_the_china(filename, df)

        # 用户特征性别分布
        # gender_distribution(filename, df)

        # 用户认证类型分布
        # authentication_type(filename, df)

        # 粉丝数量区间分布
        # number_of_fans_distributions(filename, df)

    else:
        # 测试全部文件
        for filename in filenames:
            print(f"文件名 : {filename}")

            df = pd.read_csv(DATA_DIR + filename, encoding='gb18030')

            # 数据集微博总数, 重复总数
            # repeat_tweets = number_of_repeat_tweets(df)

            # 删除重复的推文(后续有些函数如需使用删除微博分析, 可以将该语句注释去除, 但是运行较慢)
            # df = delete_repeat_tweets(df, repeat_tweets)

            # 文件中数据的采集时间
            # collection_time(df)

            # 分析原始非微博数据, 此时需要修改DATA_DIR = 'data_non_weibo/'
            # non_weibo_data_analysis(df)
        
            # 分析非微博数据中媒体类型分布
            # media_type_distribution(filename, df)
        
            # 分析非微博数据中媒体名称排名
            # media_name_distribution(filename, df)

            # 利用原始数据构造事件扩散网络(是否删除重复推文对构造网络无影响)
            # csv2adjlist(filename, df, RESULT_DIR)

            # 对于图分析, 需要临时修改一下路径
            # filename = RESULT_DIR + 'adjlist/' + filename.replace('.csv', '.adjlist')
            # analyze_graph(filename)

            # 分析事件传播速率和传播规模曲线
            # calculate_diffusion_rate(filename, df)

            # 分别观察转发和原创两种类型微博数量随着时间变化的曲线
            # analyze_diffusion_line(filename, df)

            # 分析事件新奇性
            # analyze_novel(filename, df)

            # 分析用户对事件的情绪
            # analyze_emotion(filename, df)

            # 分析用户的情绪演进
            # emotion_evolution(filename, df)
        
            # 国内外分布
            # event_spatial_distribution_in_the_world(filename, df)

            # 国内各省市分布 分原创和转发
            # event_spatial_distribution_in_the_china(filename, df)

            # 用户特征性别分布
            # gender_distribution(filename, df)

            # 用户认证类型分布
            # authentication_type(filename, df)

            # 粉丝数量区间分布
            # number_of_fans_distributions(filename, df)

    print(f"The Spent time : {time.time() - start_time:.2f}s")

if __name__ == '__main__':
    main()

