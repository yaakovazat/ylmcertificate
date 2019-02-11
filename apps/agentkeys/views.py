from django.shortcuts import render
from .models import Agent
from datetime import datetime
import re
# Create your views here.R
def getkey(request):
    context = {}
    if(request.method =='POST'):
        telephone = request.POST.get('telephone')
        if(re.match(r'1[3,4,5,7,8]\d{9}',telephone)):
            telNumStatus = '1'
        else:
            telNumStatus = '0'
        (telephone.strip(' ')).strip('\n')
        # print(telephone)
        dt = datetime.now()
        key = dt.strftime("%m%d%H%M%S")
        # print(key)

        agent = Agent()

        if(telNumStatus=='1'):
            agent.telephone = telephone
            context['value'] = key
            agent.key = key
            agent.save()
        else:
            context['value'] = '手机号不合法!'

    return render(request,'generate_key.html',context)