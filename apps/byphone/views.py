from django.shortcuts import render
import json
from azat import ROOT_DIR
from datetime import datetime
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
        dt = datetime.now()
        keytime = dt.strftime("%m%d%H%M%S")
        # if (telNumStatus == '1'):
        #     ddinfo['value'] = key
        # else:
        #     ddinfo['value'] = '手机号不合法!'

    return render(request,'byphone.html',{'LastTime':keytime})
