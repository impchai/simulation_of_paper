# -*- coding: UTF-8 -*-
import numpy as np
import math
import random
from random import choice
#from scipy import integrate
import random
import xlwt
import matplotlib.pyplot as plt
import networkx as nx


# import pyglet
G = nx.DiGraph()
pos = []
NODES = 0
node_id = []
def init(N_block_init):
    #####  Definition #####################################
    v_init_info = np.zeros(
        N_block_init, dtype=[('id', np.int8), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                             ('m', np.float32), ('posx', np.int8 ), ('posy', np.float32 )])

    v_candidate_info = np.zeros(
        [], dtype=[('id', np.int8), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                   ('m', np.float32), ('posx', np.int8 ), ('posy', np.float32 )]) #当前时刻的 候选者集合
    v_candidate_info_ = np.zeros(
        [], dtype=[('id', np.int8), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                   ('m', np.float32), ('posx', np.int8 ), ('posy', np.float32 )]) #下一时刻的 候选者集合
    #####   Initial ICVs  #####################

    v_init_info['id'] = np.arange(1, N_block_init + 1) #初始块id  1~99
    v_init_info['a'] = np.random.rand(N_block_init)
    v_init_info['b'] = np.random.rand(N_block_init)*2-1
    v_init_info['c'] = np.random.rand(N_block_init)

    # v_init_info['m'] = (v_init_info['a']*(1-v_init_info['c'])+v_init_info['b']*v_init_info['b'])/2
    v_init_info['m'] = np.linspace(0,0.8,N_block_init)
    v_init_info['posx'] = np.ones( N_block_init )
    v_m_mean = sum(v_init_info['m'])/N_block_init
    v_init_info['posy'] = np.argsort(v_init_info['m'])
    v_init_info['posy'] = v_init_info['m']
    v_candidate_info = v_init_info
    v_candidate_info_ = v_init_info
    for v in range(N_block_init):
        G.add_node(v, desc = v_init_info['id'][v])
        node_id.append(v_init_info['id'][v])
        pos.append( (int(v_init_info['posx'][v]), (v_init_info['posy'][v])) )
    NODES = G.number_of_nodes()

    return NODES, v_candidate_info,v_candidate_info_, v_m_mean

def get_result( N_join_max, N_join_min, N_times, NODES, v_candidate_info,v_candidate_info_,v_m_mean,N_block_init ):
    v_join_info = np.zeros(
        [N_times, N_join_max], dtype=[('id', np.int8), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                                      ('m', np.float32), ('posx', np.int8), ('posy', np.float32)])
    for i in range(N_times):
        n_number = np.random.randint(N_join_min, N_join_max)
        # n_number = N_times-i
        p_candidate = np.zeros([n_number, len(v_candidate_info)])
        temp_p = np.zeros([n_number, len(v_candidate_info)])
        v_choice_id = np.zeros([n_number, 2])
        v_join_info[i]['id'][0: n_number] =(i + 1) * 100 + np.arange(1, n_number + 1)  # 第n轮到达车辆id = n*100 + 1~99
        v_join_info[i]['a'][0: n_number] = np.random.rand(n_number)
        v_join_info[i]['b'][0: n_number] = np.random.rand(n_number)*2-1
        v_join_info[i]['c'][0: n_number] = np.random.rand(n_number)

        v_join_info[i]['m'] = (v_join_info[i]['a'] * (1 - v_join_info[i]['c']) + v_join_info[i]['b'] * v_join_info[i]['b']) / 2
        v_join_info[i]['posx'][0: n_number] = np.ones(n_number)*(i + 2)
        v_m_mean_join = sum(v_join_info[i]['m'][0: n_number]) / n_number
        k = (N_block_init/2)/v_m_mean*v_m_mean_join
        v_join_info[i]['posy'][0: n_number] = v_join_info[i]['m'][0: n_number]
        print('pos:',v_join_info[i]['m'])
        for v in range(n_number):
            G.add_node(NODES+ v , desc=v_join_info[i]['id'][v])
            node_id.append(v_join_info[i]['id'][v])
            pos.append(( int(v_join_info[i]['posx'][v]), (v_join_info[i]['posy'][v]) ))
        NODES = G.number_of_nodes()

        for v in range(n_number):


            data = np.exp(-beta*(v_candidate_info['m'] - v_join_info[i][v]['m'])*(v_candidate_info['m'] - v_join_info[i][v]['m']))
            data2 = data / (sum(data))
            p_candidate[v] = data2
            p_candidate[v] /= p_candidate[v].sum()

            v_choice_id[v] = np.random.choice(v_candidate_info['id'], 2, p=p_candidate[v], replace=False)

            G.add_edge(node_id.index(v_join_info[i]['id'][v]), node_id.index(v_choice_id[v][0]))
            G.add_edge(node_id.index(v_join_info[i]['id'][v]), node_id.index(v_choice_id[v][1]))
            v_candidate_info_ = np.delete(v_candidate_info_, v_candidate_info_['id'] == v_choice_id[v][0])#删除被选择的块id
            v_candidate_info_ = np.delete(v_candidate_info_, v_candidate_info_['id'] == v_choice_id[v][1])
            v_candidate_info_ = np.append(v_candidate_info_, v_join_info[i][v]) #添加新增的块id


        v_candidate_info = v_candidate_info_

    number_candidate = len(v_candidate_info)
    return number_candidate


w = xlwt.Workbook()
ws = w.add_sheet('Hey, Hades')

N_block_init = 12 #
N_join_max =8 #
N_join_min = 6 #
N_times = 1  #
beta= 0.05
y = []
y.append(N_block_init)
NODES, v_candidate_info,v_candidate_info_ ,v_m_mean= init(N_block_init)
print(pos)

for x in range(1):
    N_times = 10
    result = get_result(N_join_max, N_join_min, N_times,NODES, v_candidate_info,v_candidate_info_,v_m_mean,N_block_init)


font1 = {'family' : 'Times New Roman',

'weight' : 'normal',

'size' : 20,

}

nx.draw_networkx(G, pos, with_labels=None,node_size = 50, width = 0.5)
plt.xlabel("Transaction Rounds",font1)
plt.ylabel("Sites with Descending m",font1)





plt.show()











