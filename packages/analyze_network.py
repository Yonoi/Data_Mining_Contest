'''
1. 分析由create_network生成的事件扩散网络
2. 分析i级转发节点(包括扩散深度和广度)
作者 : Mingjie
时间: 2021年4月1日
'''
import collections
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from itertools import chain

def search_neighbors(nodes, G, k):
    '''
    在图Ｇ中找第i-1级的节点的第i级的邻居
    返回找的邻居集合
    '''
    neighbors_nodes = list(chain(*[list(G.neighbors(node)) for node in nodes]))

    # 断言是否找的正确
    # assert list(dict(G.in_degree(neighbors_nodes)).values()) == [1] * len(neighbors_nodes)

    print(f"The {k:2}th level nodes : {len(neighbors_nodes)}")
    return neighbors_nodes

def draw(l1, filename):
    '''
    对分析结果绘图
    '''
    x = np.arange(0, len(l1))
    plt.plot(x, l1, color='orange', marker='+')
    plt.title(f"{filename.replace('.adjlist', '').replace('res/adjlist/', '') + '--i级转发分布'}")
    plt.xlabel("i级转发")
    plt.ylabel("节点总数")
    for a, b in zip(x, l1):
        plt.text(a, b + 0.05, b, ha='left', va='bottom', color='blue')
    print(filename)
    plt.savefig(f"{'res/images/' + 'i级转发分布--' + filename.replace('.adjlist', '').replace('res/adjlist/', '')}", dpi=800)
    print(f"{'res/images/' + 'i级转发分布--' + filename.replace('.adjlist', '.png').replace('res/adjlist/', '')}")
    plt.show()

def analyze_graph(filename):
    G = nx.read_adjlist(filename, create_using=nx.DiGraph())

    print(f"nodes : {G.number_of_nodes()}")
    print(f"edges : {G.number_of_edges()}")

    # 孤立节点: 1) 采集时间内, 原创无转发. 2)采集时间外, 只被采集时间内的节点引用.
    print(f"isolates : {nx.number_of_isolates(G)}")

    # 测试: 度分布直方图
    # degree = nx.degree_histogram(G)
    # print(degree)
    
    # 第一级节点, 包含孤立节点和无入度有出度的节点
    G.remove_nodes_from(list(nx.isolates(G))) # 删除孤立节点
    init_nodes = [node for node, degree in G.in_degree() if degree==0]
    print(f"The {0:2}th level nodes : {len(init_nodes)}")

    # 迭代深度, 访问每层节点数目.
    nodes = init_nodes
    number_of_the_ith_level_nodes = [len(nodes)]
    k = 1
    while True:
        neighbors = search_neighbors(nodes, G, k)
        if len(neighbors) == 0:
            break
        nodes = neighbors
        number_of_the_ith_level_nodes.append(len(nodes))
        k += 1

    draw(number_of_the_ith_level_nodes, filename)


