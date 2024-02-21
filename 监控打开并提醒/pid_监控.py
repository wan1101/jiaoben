import psutil

for pnum in psutil.pids():

    p = psutil.Process(pnum)

    # print(u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s "
    #       % (p.name(), p.memory_percent(), p.status(), p.create_time()))
    if p.name() == "WeChat.exe":
        print("进程状态%-10s" % p.status())
        print("线程开启数量%d" % p.num_threads())
        print(p)

