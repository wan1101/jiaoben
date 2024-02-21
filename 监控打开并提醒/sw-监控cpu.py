#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import psutil


class MonitorCPUMemory():

    def __init__(self):
        pass

    def write(self, text1, text2, text3):
        """写入log中"""
        timer = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('text.log', 'a+', encoding='utf-8') as tf:
            text = timer + "  内存占用率= {}% ，软件cpu使用率为 {}%，系统cpu使用率为 {}%\n".format(text1, text2, text3)
            tf.write(text)

    def CM_monitor(self):
        """CPU+内存监控"""
        for i in psutil.pids():
            pid = psutil.Process(i)
            if pid.pid == 10956:  # 这里修改索要监控的pid
                while True:
                    a = pid.memory_percent()  # 内存占用%
                    b = pid.cpu_percent()
                    c = psutil.cpu_percent()
                    time.sleep(1)
                    self.write(a, b, c)


if __name__ == '__main__':
    a = MonitorCPUMemory()
    a.CM_monitor()


