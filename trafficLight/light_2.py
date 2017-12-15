import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading
import pickle

def read_data(filepath):
    with open(filepath, 'rb') as f:
        data = pickle.load(f)

    return data

class optimize(object):
    def __init__(self):
        # state 1-5
        #
        self._cars = [{'count':0,
                       '1_count':0, '1_stop_coef':0, '2_count':0, '2_stop_coef':0,
                       '3_count':0, '3_stop_coef':0, '4_count':0, '4_stop_coef':0,
                       '5_count':0, '5_stop_coef':0}
                      for i in range(7)]


    def cal_stop_coef(self, data):
        for i in range(7):
            self._cars[i]['count'] = data[i]['count']


if __name__ == '__main__':
    state = {'y1_1':0, 'y1_2':0, 'y1_3':0,
              'y2_1': 0, 'y2_2': 0, 'y2_3': 0, 'y2_4':0,
              'y3_1': 0, 'y3_2': 0, 'y3_3': 0,
              'y4_1': 0, 'y4_2': 0, 'y4_3': 0, 'y4_4':0, 'y4_5':0,
              'y5_1': 0, 'y5_2': 0, 'y5_3': 0,
              'y6_1': 0, 'y6_2': 0, 'y6_3': 0, 'y6_4':0,
              'y7_1': 0, 'y7_2': 0, 'y7_3': 0, 'y7_4':0}
    data = read_data('../data.pkl')
    for i in range(7):
        for j in range(1, 9):
            data[i]['%d' % j] = data[i]['%d_pass' % j] + data[i]['%d_stop' % j]

    # print(data)

    state['y1_1_stop'] = data[0]['2_stop'] + data[0]['4_stop']
    state['y1_2_stop'] = data[0]['3_stop'] + data[0]['1_stop']
    state['y1_3_stop'] = data[0]['5_stop'] + data[0]['7_stop'] + data[0]['8_stop'] + data[0]['6_stop']

    state['y2_1_stop'] = data[1]['2_stop'] + data[1]['4_stop']
    state['y2_2_stop'] = data[1]['3_stop'] + data[1]['1_stop']
    state['y2_3_stop'] = data[1]['5_stop'] + data[1]['6_stop']
    state['y2_4_stop'] = data[1]['7_stop'] + data[1]['8_stop']

    state['y3_1_stop'] = data[2]['2_stop'] + data[2]['4_stop']
    state['y3_2_stop'] = data[2]['3_stop'] + data[2]['1_stop']
    state['y3_3_stop'] = data[2]['5_stop'] + data[2]['7_stop'] + data[2]['8_stop'] + data[2]['6_stop']

    state['y4_1_stop'] = data[3]['2_stop'] + data[3]['4_stop']
    state['y4_2_stop'] = data[3]['3_stop'] + data[3]['1_stop']
    state['y4_3_stop'] = data[3]['5_stop']*31/(31+19) + data[3]['6_stop']
    state['y4_4_stop'] = data[3]['5_stop']*19/(31+19) + data[3]['7_stop']*19/(19+41)
    state['y4_5_stop'] = data[3]['8_stop'] + data[3]['7_stop']*41/(19+41)

    state['y5_1_stop'] = data[4]['2_stop'] + data[4]['4_stop']
    state['y5_2_stop'] = data[4]['3_stop'] + data[4]['1_stop']
    state['y5_3_stop'] = data[4]['5_stop'] + data[4]['7_stop'] + data[4]['8_stop'] + data[4]['6_stop']

    state['y6_1_stop'] = data[5]['2_stop']*28/(28+121) + data[5]['1_stop']*28/(28+121)
    state['y6_2_stop'] = data[5]['2_stop']*121/(28+121) + data[5]['1_stop']*121/(28+121) + \
                       data[5]['3_stop']*121/(121+13) + data[5]['4_stop']*121/(121+13)
    state['y6_3_stop'] = data[5]['3_stop']*13/(121+13) + data[5]['4_stop']*13/(121+13)
    state['y6_4_stop'] = data[5]['5_stop'] + data[5]['6_stop'] + data[5]['7_stop'] + data[5]['8_stop']

    state['y7_1_stop'] = data[6]['3_stop'] + data[6]['1_stop']*111/(111+9)
    state['y7_2_stop'] = data[6]['2_stop']*9/(9+43) + data[6]['1_stop']*9/(111+9)
    state['y7_3_stop'] = data[6]['2_stop']*43/(9+43) + data[6]['4_stop']
    state['y7_4_stop'] = data[6]['5_stop'] + data[6]['6_stop'] + data[6]['7_stop'] + data[6]['8_stop']

    # file = '../state_out.txt'
    # with open(file, 'w+') as f:
    #     for (a, b) in state.items():
    #         f.write(a+' : '+str(b)+'\n')
    sum_1 =  state['y1_1_stop']+ state['y1_2_stop']+ state['y1_3_stop']
    print(str(200*state['y1_1_stop']/sum_1)+','+str(200*state['y1_2_stop']/sum_1)+','+str(200*state['y1_3_stop']/sum_1)+'\n')

    sum_2 = state['y2_1_stop'] + state['y2_2_stop'] + state['y2_3_stop'] + state['y2_4_stop']
    print(str(200 * state['y2_1_stop']/sum_2) + ',' + str(200 * state['y2_2_stop']/sum_2) + ',' + str(
        200 * state['y2_3_stop']/sum_2) + ',' + str(state['y2_4_stop']/sum_2) + '\n')

    sum_3 = state['y3_1_stop'] + state['y3_2_stop'] + state['y3_3_stop']
    print(str(200 * state['y3_1_stop'] / sum_3) + ',' + str(200 * state['y3_2_stop'] / sum_3) + ',' + str(
        200 * state['y3_3_stop'] / sum_3) + '\n')

    sum_4 = state['y4_1_stop'] + state['y4_2_stop'] + state['y4_3_stop']+state['y4_4_stop']+state['y4_5_stop']
    print(str(200 * state['y4_1_stop'] / sum_4) + ',' + str(200 * state['y4_2_stop'] / sum_4) + ',' + str(
        200 * state['y4_3_stop'] / sum_4)  + ',' + str(200 * state['y4_4_stop'] / sum_4) + ',' + str(200 * state['y4_5_stop'] / sum_4)+ '\n')

    sum_5 = state['y5_1_stop'] + state['y5_2_stop'] + state['y5_3_stop']
    print(str(200 * state['y5_1_stop'] / sum_5) + ',' + str(200 * state['y5_2_stop'] / sum_5) + ',' + str(
        200 * state['y5_3_stop'] / sum_5) + '\n')

    sum_6 = state['y6_1_stop'] + state['y6_2_stop'] + state['y6_3_stop'] + state['y6_4_stop']
    print(str(200 * state['y6_1_stop'] / sum_6) + ',' + str(200 * state['y6_2_stop'] / sum_6) + ',' + str(
        200 * state['y6_3_stop'] / sum_6) + ',' + str(200*state['y6_4_stop'] / sum_6)+ '\n')

    sum_7 = state['y7_1_stop'] + state['y7_2_stop'] + state['y7_3_stop']+state['y7_4_stop']
    print(str(200 * state['y7_1_stop'] / sum_7) + ',' + str(200 * state['y7_2_stop'] / sum_7) + ',' + str(
        200 * state['y7_3_stop'] / sum_7) +',' + str(200*state['y7_4_stop'] / sum_7) + '\n')



    # print(state)










