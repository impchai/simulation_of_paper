import numpy as np
import math
from scipy.io import savemat

from random import choice
#from scipy import integrate
import random
import xlwt
import matplotlib.pyplot as plt
import math
# import pyglet


def get_result(N_block_init, N_join_max, N_join_min, N_times):
    v_init_info = np.zeros(
        N_block_init, dtype=[('id', np.float32), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                             ('m', np.float32)])
    v_join_info = np.zeros(
        [N_times, N_join_max], dtype=[('id', np.float32), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                                      ('m', np.float32)])
    v_candidate_info = np.zeros(
        [], dtype=[('id', np.float32), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                   ('m', np.float32)])
    v_candidate_info_ = np.zeros(
        [], dtype=[('id', np.float32), ('a', np.float32), ('b', np.float32), ('c', np.float32),
                   ('m', np.float32)])

    v_init_info['id'] = np.arange(1, N_block_init + 1)
    v_init_info['a'] = np.random.rand(N_block_init)
    v_init_info['b'] = np.random.rand(N_block_init)
    v_init_info['c'] = np.random.rand(N_block_init)
    v_init_info['m'] = (v_init_info['a']*(1-v_init_info['c'])+v_init_info['b']*v_init_info['b'])/2

    v_candidate_info = v_init_info
    v_candidate_info_ = v_init_info
    x=[]
    x.append(N_block_init)

    for i in range(N_times): #到达N_times轮
        #You can Choose different distributions of tip arrival Here#
        # n_number = np.random.randint(N_join_min, N_join_max) #Randim Distribution
        # n_number = np.random.poisson(lam=700,size=1)[0]#Poisson Distribution
        n_number = int(np.random.gamma(200, 1, 10)[0])#Gamma Distribution
        p_candidate = np.zeros([n_number, len(v_candidate_info)])
        temp_p = np.zeros([n_number, len(v_candidate_info)])
        v_choice_id = np.zeros([n_number, 2])
        v_join_info[i]['id'][0: n_number] = (i + 1) * 100 + np.arange(1, n_number + 1) # 第n轮到达车辆id = n*100 + 1~99
        v_join_info[i]['a'][0: n_number] = np.random.rand(n_number)
        v_join_info[i]['b'][0: n_number] = np.random.rand(n_number)
        v_join_info[i]['c'][0: n_number] = np.random.rand(n_number)
        v_join_info[i]['m'] = (v_join_info[i]['a'] * (1 - v_join_info[i]['c']) + v_join_info[i]['b'] * v_join_info[i]['b']) / 2
        for v in range(n_number):
            beta=0.005
            data = np.exp(-beta*(v_candidate_info['m'] - v_join_info[i][v]['m'])*(v_candidate_info['m'] - v_join_info[i][v]['m']))
            data2 = data / (sum(data))
            p_candidate[v] = data2
            p_candidate[v] /= p_candidate[v].sum()
            v_choice_id[v] = np.random.choice(v_candidate_info['id'], 2, p=p_candidate[v], replace=False)
            v_candidate_info_ = np.delete(v_candidate_info_, v_candidate_info_['id'] == v_choice_id[v][0])#删除被选择的块id
            v_candidate_info_ = np.delete(v_candidate_info_, v_candidate_info_['id'] == v_choice_id[v][1])
            v_candidate_info_ = np.append(v_candidate_info_, v_join_info[i][v])

        v_candidate_info = v_candidate_info_
        print(len(v_candidate_info))
        x.append(len(v_candidate_info))


    number_candidate = len(v_candidate_info)

    return number_candidate,x


w = xlwt.Workbook()
ws = w.add_sheet('Hey, Hades')

N_block_init = 1000
N_join_max = 1000
N_join_min = 500
# N_times = 1  #到达车辆轮数总数
arf = 1
y = []

N_times = 50
result, y = get_result(N_block_init, N_join_max, N_join_min, N_times)
f_name='gam_high.mat'
savemat(f_name, {'high':y})

print(y)

plt.plot(y)
plt.show()








