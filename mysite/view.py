from django.http import HttpResponse,Http404
import datetime
from django import template
from django.template import loader,Context

def current_datetime(req):
    now=datetime.datetime.now()
    fp=open('E:/kaifa/SEA/pangdudu/6/templates/pachong.html')
    t=template.Template(fp.read())
    fp.close()
    html=t.render(template.Context({'current_date':now}))
    return HttpResponse(html)
def ctime(req,num):
    try:
        num=int(num)
        num=str(num)
    except ValueError:
        raise  Http404
    txt="url is [http://127.0.0.1:8000/time/%s/]" % num
    #cutime=datetime.datetime.now()
    #txt="it's %s."% cutime
    return HttpResponse(txt)
def hello(req):
    return  HttpResponse("<h1>Hello World! WeiXin</h1>")
def homepage(req):
    return  HttpResponse("this is homepage!")
