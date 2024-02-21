import os
import time
import psutil as psutil
import email_tools


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleeptime(0, 0, 2)  # 每2秒执行一次
while True:
    time.sleep(second)
    print('正在检查程序中......')

    pidnum = 0

    for proc in psutil.process_iter():
        if proc.name() == "msedge.exe":
            print("pid-%d,name:%s" % (proc.pid, proc.name()))
            pidnum = pidnum + 1
            print(pidnum)
    if pidnum >= 6:
        print('进程数正常')
         # os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    else:
        print("进程数不正常")
        email_tools.email()














# pidnum = 0
#
# for proc in psutil.process_iter():
#     if proc.name() == 'msedge.exe':
#         print("pid-%d,name:%s" % (proc.pid, proc.name()))
#         pidnum = pidnum + 1
#         print(pidnum)
#         if pidnum <= 6:
#             if proc.name() =='msedge.exe':
#                 print('进程不足6个，正在发送邮件通知....')
#                 email_tools.email()
#                 os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
#             else:
#                 print("进程数正常")

