from django.shortcuts import render
import re
import json
from azat import ROOT_DIR
from datetime import datetime
from data.update import fn
# Create your views here.
def phone(request):
    # ddinfo={}
    if(request.method == 'POST'):
        telephone = request.POST.get('telephone')
        if (re.match(r'1[3,4,5,7,8]\d{9}', telephone)):
            telNumStatus = '1'
        else:
            telNumStatus = '0'
        (telephone.strip(' ')).strip('\n')
        # if (telNumStatus == '1'):
        #     ddinfo['value'] = key
        # else:
        #     ddinfo['value'] = '手机号不合法!'
        dt = datetime.now()
        keytime = dt.strftime("%m%d%H%M%S")
    return render(request,'byphone.html',{'ddinfo':telephone , 'message':keytime})
