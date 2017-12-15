import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading
import pickle

def which_road(x, y):
    '''
    if x in range(521365, 521427) and y in range(53259, 53988):
        return 1
    elif x in range(520916, 521365) and y in range(53847, 54053):
        return 2
    elif x in range(521427, 521958) and y in range(53815, 54101):
        return 3

    elif x in range(521365, 521425) and y in range(53988, 54891):
        return 4
    elif x in range(520916, 521413) and y in range(54688, 54990):
        return 5
    elif x in range(521425, 521958) and y in range(54688, 55212):
        return 6

    elif x in range(521413, 521434) and y in range(54891, 55875):
        return 7
    elif x in range(520916, 521420) and y in range(55736, 56006):
        return 8
    elif x in range(521434, 521958) and y in range(55323, 55958):
        return 9

    elif x in range(521420, 521460) and y in range(55875, 56676):
        return 10
    elif x in range(520916, 521447) and y in range(56562, 56783):
        return 11
    elif x in range(521460, 521958) and y in range(56451, 56783):
        return 12

    elif x in range(521449, 521523) and y in range(56676, 57071):
        return 13
    elif x in range(520916, 521512) and y in range(56975, 57165):
        return 14
    elif x in range(521523, 521958) and y in range(56975, 57165):
        return 15

    elif x in range(521512, 521590) and y in range(57071, 57519):
        return 16
    elif x in range(520916, 521512) and y in range(57387, 57626):
        return 17

    elif x in range(521579, 521681) and y in range(57519, 58129):
        return 19
    elif x in range(520916, 521672) and y in range(57959, 58388):
        return 20
    elif x in range(521681, 521958) and y in range(57959, 58388):
        return 21

    elif x in range(521672, 521759) and y in range(58129, 58880):
        return 22
    else:
        return 0
    '''

    if (x >= 521365 and x < 521427) and (y >= 53259 and y < 53988):
        return 1
    elif (x >= 520916 and x < 521365) and (y >= 53847 and y < 54053):
        return 2
    elif (x >= 521427 and x < 521958) and (y >= 53815 and y < 54101):
        return 3

    elif (x >= 521365 and x < 521425) and (y >= 53988 and y < 54891):
        return 4
    elif (x >= 520916 and x < 521413) and (y >= 54688 and y < 54990):
        return 5
    elif (x >= 521425 and x < 521958) and (y >= 54688 and y < 55212):
        return 6

    elif (x >= 521413 and x < 521434) and (y >= 54891 and y < 55875):
        return 7
    elif (x >= 520916 and x < 521420) and (y >= 55736 and y < 56006):
        return 8
    elif (x >= 521434 and x < 521958) and (y >= 55323 and y < 55958):
        return 9

    elif (x >= 521420 and x < 521460) and (y >= 55875 and y < 56676):
        return 10
    elif (x >= 520916 and x < 521447) and (y >= 56562 and y < 56783):
        return 11
    elif (x >= 521460 and x < 521958) and (y >= 56451 and y < 56783):
        return 12

    elif (x >= 521449 and x < 521523) and (y >= 56676 and y < 57071):
        return 13
    elif (x >= 520916 and x < 521512) and (y >= 56975 and y < 57165):
        return 14
    elif (x >= 521523 and x < 521958) and (y >= 56975 and y < 57165):
        return 15

    elif (x >= 521512 and x < 521590) and (y >= 57071 and y < 57519):
        return 16
    elif (x >= 520916 and x < 521512) and (y >= 57387 and y < 57626):
        return 17

    elif (x >= 521579 and x < 521681) and (y >= 57519 and y < 58129):
        return 19
    elif (x >= 520916 and x < 521672) and (y >= 57959 and y < 58388):
        return 20
    elif (x >= 521681 and x < 521958) and (y >= 57959 and y < 58388):
        return 21

    elif (x >= 521672 and x < 521759) and (y >= 58129 and y < 58880):
        return 22
    else:
        return 0

class Cars(object):
    def __init__(self, filePath):
        self.filePath = filePath
        data = pd.read_csv(self.filePath, index_col=False)
        self.data = data
        self._index_epoch = 0
        self.length = len(self.data)
        # return data['x-coordinate'][25:50], data['y-coordinate'][25:50], data['speed'][:25], data['category'][:25]

    def get_data(self):
        return self.data['x-coordinate'], self.data['y-coordinate'], self.data['speed'], self.data['category']

    def plot_all_car(self):

        plt.figure()
        plt.scatter(self.data['x-coordinate'], self.data['y-coordinate'], s=0.1)

        plt.show()

    def plot_car(self, x, y):
        plt.figure()
        plt.scatter(x, y, s=0.1)

        plt.show()

    def reset_batch_index(self):
        self._index_epoch = 0


    def next_batch(self):
        if self._index_epoch == self.length:
            return list([1])

        next_epoch = self._index_epoch
        while(next_epoch < self.length and self.data['vehicle-id'][next_epoch] == self.data['vehicle-id'][self._index_epoch]):
            next_epoch += 1

        ori_epoch = self._index_epoch
        self._index_epoch = next_epoch
        return self.data.loc[ori_epoch: next_epoch-1]

    def get_direction(self):
        data = self.next_batch()


class Crossroads(object):
    def __init__(self):
        # 7 cross_roads
        # 1_stop: 方向1被阻塞的概率
        # 1_count: 路口1的车流量
        self._crosses = [dict({'count': 0,
                              '1_pass': 0, '1_stop': 0, '2_pass': 0, '2_stop': 0,
                              '3_pass': 0, '3_stop': 0, '4_pass': 0, '4_stop': 0,
                              '5_pass': 0, '5_stop': 0, '6_pass': 0, '6_stop': 0,
                              '7_pass': 0, '7_stop': 0, '8_pass': 0, '8_stop': 0,}) for i in range(8)]

    @property
    def crosses(self):
        return self._crosses

    def count_block(self, x, y, speed):
        length = len(x)

        if length == 0:
            return

        if(type(x) != list):
            x = list(x)
            y = list(y)
            speed = list(speed)

        start_road = which_road(x[0], y[0])
        end_road = which_road(x[-1], y[-1])
        if(start_road == end_road):
            return
        else:
            # 依次判断三个，要是全是一样，则判断为转弯，若到了最后两个数据不一样，也判断为转弯
            # 若发现停止x (x为speed==0的个数，可以换算成时间) 次，则计数x次，然后在下个路口的 n_stop += x/length, n_pass += 1-n_stop
            # 若没有发现停止，则 n_pass += 1
            # 然后将路口的车count += 1

            # 1_stop: 路口1被阻塞的概率
            # 1_count: 路口1的车流量
            start = start_road
            stop_length = 0
            pass_length = 0
            total_length = 0

            for i in range(length):
                temp = which_road(x[i], y[i])

                if temp == 0:
                    continue

                if start == temp:
                    if(speed[i] == 0.0):
                        stop_length += 1
                    else:
                        pass_length += 1
                    total_length += 1

                else:
                    if total_length == 0:
                        continue
                    if(i < length - 2 and temp == which_road(x[i+1], y[i+1]) and temp == which_road(x[i+2], y[i+2]) or
                       i == length - 2 and temp == which_road(x[i+1], y[i+1])):
                        self.classify_direction_crossroad(start, temp, stop_length/total_length, pass_length/total_length)

                        stop_length = 0
                        pass_length = 0
                        total_length = 0
                        start = temp

    def classify_direction_crossroad(self, start, end, stop_per, pass_per):
        # 防止有段数据丢失，跳变到另一个路段这种情况直接跳过不判断（还没写好）
        '''
        if ((start-1) / 3 != (end-1) / 3):
            if((start > end and (start) % 3 > 1) or (start < end and (end) % 3 > 1)):
                return
        '''
        crossroad = self.which_crossroad(start, end)
        print(start, end, crossroad)
        temp_direction_start = start - 3 * (crossroad-1)
        temp_direction_end = end - 3 * (crossroad-1)
        print(temp_direction_start, temp_direction_end)

        # 为了好看，这里直接枚举所有
        # ↑:1  ↑←: 2  ↓:3  ↓→:4  →↑:5  ←↓:6  →:7  ←:8
        temp_index = {-3:2, -7:1, -4:7, -6:5, 1:6, -1:8, 2:3, -2:4}
        temp = temp_direction_start - temp_direction_end*2

        try:
            self._crosses[crossroad]['%d_pass' % (temp_index[temp])] += pass_per
            self._crosses[crossroad]['%d_stop' % (temp_index[temp])] += stop_per
            self._crosses[crossroad]['count'] += 1
        except:
            pass

    def which_crossroad(self, start, end):
        temp_start = (start-1) / 3
        temp_end = (end - 1) / 3
        road_index = (temp_end + temp_start)//2 + 1

        return int(road_index)


if __name__ == '__main__':

    # 假设所有的车辆都没有重复

    print(which_road(521545, 57251.4))

    cars = Cars('../didi/data.txt')
    cars.plot_all_car()
    # x, y, speed, category = g.get_data()
    car_epoch = cars.next_batch()
    crossroad = Crossroads()
    # f = plt.figure()
    color = ['r', 'b', 'black', 'g']
    i = 0
    while type(car_epoch) != list:
        # plt.figure()
        # plt.scatter(car_epoch['x-coordinate'], car_epoch['y-coordinate'], s=1, c=color[i])
        crossroad.count_block(car_epoch['x-coordinate'], car_epoch['y-coordinate'], car_epoch['speed'])
        car_epoch = cars.next_batch()
        i += 1
    for i in range(8):
        print(crossroad.crosses[i])

    # plt.show()
    with open('../data.pkl', 'wb') as f:
        pickle.dump(crossroad.crosses[1:], f)

# 尝试多线程解决问题
'''
class plt_show(threading.Thread):
    def __init__(self, x, y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        plt.figure()
        plt.scatter(self.x, self.y)

        plt.show()
'''




