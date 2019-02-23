from datetime import datetime

dt = datetime.now()
UpdatedTime = dt.strftime("20%y年%m月%d日%H时%M分")
print("本次更新时间为:%s"%UpdatedTime)