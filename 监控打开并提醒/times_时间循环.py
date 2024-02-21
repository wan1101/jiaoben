#	时间循环

import time


def sleeptime(hour, min, sec):
     return hour * 3600 + min * 60 + sec


second = sleeptime(0, 0, 2)  # 每2秒执行一次

while True:
    time.sleep(second)
    print('正在循环中')

