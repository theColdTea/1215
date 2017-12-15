import pandas as pd

#
# import threading, time
# def Myjoin():
#     print('hello world!')
#     time.sleep(1)
# for i in range(5):
#     t=threading.Thread(target=Myjoin)
#     t.start()
#     # t.join()
# print('hello main')


a = dict({})

a[1] = 3

d = pd.DataFrame([22])

_crosses = [dict({'count': 0,
                              '1_pass': 0, '1_stop': 0, '2_pass': 0, '2_stop': 0,
                              '3_pass': 0, '3_stop': 0, '4_pass': 0, '4_stop': 0,
                              '5_pass': 0, '5_stop': 0, '6_pass': 0, '6_stop': 0,
                              '7_pass': 0, '7_stop': 0, '8_pass': 0, '8_stop': 0,}) for i in range(8)]
print(_crosses)