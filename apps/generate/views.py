from django.shortcuts import render
from agentkeys.models import Agent
from .typeW import typeWords
from azat import ROOT_DIR
import os
from status.models import Bridge
import json
# Create your views here.
# print(os.path.abspath(__file__))
def certificate(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        idcard = request.POST.get('ID')
        wechat = request.POST.get('Wechat_ID')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        work_place = request.POST.get('workPlace')
        message = request.POST.get('message')
        if(name!='' and idcard!='' and wechat!='' and email!='' and address!='' and profession!='' and work_place!='' and message!=''):
            with open(os.path.join(ROOT_DIR,"log/current.json")) as f:
                current = json.loads(f.read())
            key_num = current['key']
            image_src = typeWords(name,idcard,key_num)
            # image_src = "static/image/certificates/%s.png"%key_num
            # print(image_src)
            agent = Agent()
            agent.telephone =current['telephone']
            agent.key = key_num
            agent.name = name
            agent.idcard = idcard
            agent.wechat = wechat
            agent.address = address
            agent.email = email
            agent.profession = profession
            agent.work_place = work_place
            agent.message = message
            agent.certificate = image_src
            image_link="/image/certificates/%s.png"%key_num
            agent.save()
            img=str(image_link)

            return render(request,'status.html',{'message':'提交成功!\n 一路梦机器人正在为您制作您的授权书\n 请你稍等片刻!', 'image':img})
        else:
            return render(request,'status.html',{'message':"您好亲!\n需要填写所有必要信息\n方可获取申请书!!",'image':'/image/default.png'})
    return render(request, 'certificate.html')

