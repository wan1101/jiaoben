# -*- coding:utf-8 -*-
# @Time   : 2022-01-24
# @Author : carl_DJ

from win10toast import ToastNotifier
import time
toaster = ToastNotifier()

#基本信息设置
header = input("需要提醒的信息\n")
text = input("相关信息\n")
time_min=float(input("多少时间内提醒?\n"))

time_min = time_min * 60
print("设置提醒..")
time.sleep(2)
print("全部设置!")
time.sleep(time_min)
toaster.show_toast(f"{header}", f"{text}", duration=10, threaded=True)
while toaster.notification_active():
	time.sleep(0.005)

