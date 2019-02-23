# from datetime import datetime
from datetime import datetime


import threading as thd

def fn():
    dt = datetime.now()
    updatedTime = dt.strftime("20%y年%m月%d日%H时%M分")
    thd.Timer(10, fn).start()
    return UpdatedTime

UpdatedTime = fn()
print("本次更新时间为:%s"%UpdatedTime)