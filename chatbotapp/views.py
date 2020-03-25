from django.shortcuts import render
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbotapp.models import Message
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now as utcnow
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    context = dict()
    return render(request, 'chatbotapp/index.html', context)

def prueba(request):
    r = Message.objects.order_by('-time')[:20]
    res = []
    for msgs in reversed(r) :
        res.append({'id':msgs.id,'msg':msgs.message,'time':msgs.time.strftime('%I:%M:%S %p').lstrip('0')})

    data = json.dumps(res)
    # end json
    context = {'data':mark_safe(data)}
    return render(request, 'chatbotapp/prueba.html', context)


    # context = dict()
    # return render(request, 'chatbotapp/prueba.html', context)

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        d = json.loads(request.body)
        msg =  d.get('msg')
        m = Message(message=msg)
        m.save()

        res = {'id':m.id,'msg':m.message,'time':m.time.strftime('%I:%M:%S %p').lstrip('0')}
        data = json.dumps(res)
        return HttpResponse(data,content_type="application/json")


    # get request
    r = Message.objects.order_by('-time')[:20]
    res = []
    for msgs in reversed(r) :
        res.append({'id':msgs.id,'msg':msgs.message,'time':msgs.time.strftime('%I:%M:%S %p').lstrip('0')})
    
    data = json.dumps(res)

    
    return HttpResponse(data,content_type="application/json")

