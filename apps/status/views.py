from django.shortcuts import render
from agentkeys.models import Agent
from .models import Bridge
from .log import logCurrent
# Create your views here.

def get_status(request):
    loged_agent = Bridge()
    if(request.method == 'POST'):
        key_input = request.POST.get('key')
        keys_in_db = Agent.objects.all().values('key')
        keys = list()
        for key in keys_in_db:
            keys.append(key['key'])
        if(key_input in keys):
            agents = Agent.objects.filter(key=key_input)
            # print(agents.values())
            for agent in agents.values():
                telephone = agent['telephone']
                loged_agent.touch_key=key_input
                loged_agent.save()

            logCurrent(key_input,telephone)

            return render(request,'certificate.html',{'key':key_input, 'telephone':telephone})
        else:
            return render(request, 'status.html',{'message':'很抱歉!我们无法核实您的代理状态!\n 请您检查您的授权码或者联系一路梦客服!','image':'/image/default.png'})

# def home(request):
#     return render(request,'status.html')