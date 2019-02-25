from django.shortcuts import render
import re
from azat import ROOT_DIR
from datetime import datetime
from .models import Order
from .models import LastUpdateTime
import xlrd
from xlrd import xldate_as_tuple
from data.update import fn
# Create your views here.


def phone(request):
    if(request.method == 'POST'):
        telephone = request.POST.get('telephone')
        if (re.match(r'1[3,4,5,7,8]\d{9}', telephone)):
            telNumStatus = '1'
        else:
            telNumStatus = '0'
        (telephone.strip(' ')).strip('\n')
        ### time update
        time_in_db = LastUpdateTime.objects.all()
        for each in time_in_db:
            update_time = each['last_update_hand']
        ###
        if (telNumStatus == '1'):
            ddinfo['value'] = key
        else:
            ddinfo['value'] = '手机号不合法!'
        dt = datetime.now()
        keytime = dt.strftime("%m%d%H%M%S")

    time_in_db = LastUpdateTime.objects.all().values('last_update_hand')
    update_time = time_in_db

    return render(request,'byphone.html',{'ddinfo':'订单详情' , 'message':update_time})


def xlsx(request):
    if request.method == "POST":
        msg1 = "请求 POST"
        f = request.FILES['my_file']
        type_excel = f.name.split('.')[1]
        # if 'xlsx' != type_excel:
        #     msg1 = "目前仅支持 Microsoft xlsx 文件格式!"
        #     return render(request,'xlsx.html',{'msg1':msg1})
        if('xlsx' == type_excel):
            # msg1 = " Microsoft xlsx 文件格式准确!"
            # get xlsx and read
            workbook = xlrd.open_workbook(filename=None, file_contents=f.read())
            # workbook = xlrd.open_workbook(xlsx_file)
            table = workbook.sheets()[0]
            nrows = table.nrows
            msg2 = "总共读取到 %s 条订单记录!"%nrows
            # read xlsx data
            # read the updated time first
            ## update time
            dt = datetime.now()
            keytime = dt.strftime('%Y年%m月%d日 %H时%M分%S秒')
            last_update_Value = LastUpdateTime()
            last_update_Value.unique_id = "lastUpdate"
            last_update_Value.last_update_hand = keytime
            last_update_Value.save()
            ## update time finished
            first_row = table.row_values(1)
            time_update = first_row[0]
            xlsx_data = []
            for x in range(1, nrows):
                row = table.row_values(x)
                ntel = int(row[3])
                time_local_get = xldate_as_tuple(row[9], 0)
                time_local_done = xldate_as_tuple(row[10], 0)
                dt_get = datetime(*time_local_get).strftime('%Y年%m月%d日 %H时%M分%S秒')
                dt_done = datetime(*time_local_done).strftime('%Y年%m月%d日 %H时%M分%S秒')
                xlsx_data.append({
                    "data_updated": time_update,  # 更新时间
                    "ID": row[1],  # 订单编号
                    "order_name": row[2],  # 收件人 
                    "order_phone": ntel,  # 电话 
                    "order_group": row[4],  # 组别 
                    "order_detail": row[5],  # 商品简述 
                    "express": row[6],  # 快递公司 
                    "express_id": row[7],  # 快递单号 
                    "order_status": row[8],  # 订单状态 
                    "order_get_time": dt_get,  # 下单日期 
                    "order_done_time": dt_done,  # 审核日期 
                    "external_ID": row[11]  # 外部订单号 
                }
                )
                order = Order()
                for each in xlsx_data:
                    order.data_updated = each['data_updated']
                    order.ID = each['ID']
                    order.order_name = each['order_name']
                    order.order_phone = each['order_phone']
                    order.order_group = each['order_group']
                    order.order_detail = each['order_detail']
                    order.express = each['express']
                    order.express_id =each['express_id']
                    order.order_status = each['order_status']
                    order.order_get_time = each['order_get_time']
                    order.order_done_time = each['order_done_time']
                    order.external_ID = each['external_ID']
                    order.save()
                msg3 = "所有记录保存成功!"


    else:  # 当正常访问时
        msg1 = ""
        msg2 = ""
        msg3 = ""
    return render(request,'xlsx.html',{'msg1':msg1,'msg2':msg2,'msg3':msg3})
