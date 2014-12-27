# -*- coding: utf-8 -*-
import string
import urllib2
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
# Create your views here.
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({})
    #return HttpResponse('<h1>hello welcome to Django!</h1>')
    return  HttpResponse(t.render(c))
'''
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say(self):
        return "I'm " + self.name

class HTML_Tool:
    
    BgnCharToNoneRex = re.compile("(\t|\n|<a.*?>|<img.*?>)")
    
    
    EndCharToNoneRex = re.compile("<.*?>")

    
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    
    replaceTab = [("&lt;","<"),("&gt;",">"),("&amp;","&"),("&amp;","\""),("&nbsp;"," ")]
    
    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)
        #x = self.BgnPartRex.sub("\n    ",x)
        x = self.BgnPartRex.sub("\n    ",x)
        #x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNextTabRex.sub("\t",x)
        x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:  
            x = x.replace(t[0],t[1])  
        return x
class Baidu_Spider:
    
    def __init__(self):
        self.rmblist=[]
        self.salelist=[]
        self.namelist=[]
        self.myTool = HTML_Tool()
        self.num=re.compile("\d+")
        self.myPage=urllib2.urlopen('http://www.alibaba.com/product-detail/2014-New-Pvc-Bath-Duck-Bath_928667842.html').read()#.decode("gbk")
    def deal_data(self):  
        #myItems = re.findall('<a.*?href=".*?target="_blank".*?"(.*?)".*?</a>',myPage,re.S)
        myItems = re.findall('<h2 class="title"><a href=".*?" title.*? target="_blank".*?>(.*?)</a>',self.myPage,re.S)
        for item in myItems:
            item = item.replace("\n","")
            data = self.myTool.Replace_Char(item.replace("\n","").encode('gbk'))
            print data

    def deal_url(self):
        myItems3 = re.findall('<h2 class="title"><a href="(.*?)" title.*? target="_blank".*?>.*?</a>',self.myPage,re.S)
        return myItems3

    def deal_name(self):
        mes = re.findall('<h1 class="title fn" itemprop="name">(.*?)</h1>',self.myPage,re.S)
        mes=mes[0]
        mes = mes.replace("\n","")
        mes = self.myTool.Replace_Char(mes.replace("\n","").encode('gbk'))
        mes=mes.replace("'","")
        mes=mes.replace(")","")
        return mes

    def deal_wenben(self):
        mes1 = re.findall('<script type="text/javascript">.*?gdata.define.*?keyword.*?, (.*?);.*?gdata.define',self.myPage,re.S)
        mes1=mes1[0]
        mes1 = mes1.replace("\n","")
        mes1 = self.myTool.Replace_Char(mes1.replace("\n","").encode('gbk'))
        mes1=mes1.replace("'","")
        mes1=mes1.replace(")","")
        return mes1

    def deal_wenben2(self):
        mes2 = re.findall('gdata.define.*?keywords.*?, (.*?);.*?gdata.define',self.myPage,re.S)
        mes2=mes2[0]
        mes2 = mes2.replace("\n","")
        mes2 = self.myTool.Replace_Char(mes2.replace("\n","").encode('gbk'))
        mes2=mes2.replace("'","")
        mes2=mes2.replace(")","")
        return mes2

    def deal_wenben4(self):
        mes3 = re.findall('<h3 class="title">Packaging & Delivery</h3>(.*?)</table>',self.myPage,re.S)
        mes3=mes3[0]
        mes3 = self.myTool.Replace_Char(mes3.replace("\n","").encode('gbk'))
        mes3=mes3.replace("'","")
        mes3=mes3.replace(")","")
        mes3=re.sub(r'\n+','\n',mes3)
        return mes3

    def deal_wenben5(self):
        mes3 = re.findall('<h3 class="title">Specifications</h3>(.*?)</p>',self.myPage,re.S)
        mes3=mes3[0]
        mes3 = self.myTool.Replace_Char(mes3.replace("\n","").encode('gbk'))
        mes3=mes3.replace("'","")
        mes3=mes3.replace(")","")
        mes3=re.sub(r'\n+','\n',mes3)
        return mes3
"""
    def deal_wenben6(self):
        mes3 = re.findall('<div id="J-rich-text-description" class="richtext richtext-detail rich-text-description">(.*?)<script type="text/javascript">',self.myPage,re.S)
        mes3=mes3[0]
        #print mes
        #for i in range(8,1000):
            #while i*" " in mes:
                #mes = mes.replace(i*" ","")
        mes3 = self.myTool.Replace_Char(mes3.replace("\n","").encode('gbk'))
        mes3=mes3.replace("'","")
        mes3=mes3.replace(")","")
        mes3=re.sub(r'\n+','\n',mes3)
        for i in mes3:
            print i
"""

"""
def index(req,id):
    user={'name':'tom','age':23,'sex':'male'}
    book_list=['python','java','php','web']
    #user=Person('max',33,'male')
    return render_to_response ('index.html',{'title':'my pape','user':user,'book_list':book_list,'id':id})
"""
def index(req):
    mySpider = Baidu_Spider()

    mySpider.deal_name()
    mySpider.deal_wenben()
    mySpider.deal_wenben2()
    mySpider.deal_wenben4()
    mySpider.deal_wenben5()
    
    return render_to_response ('index.html',{'title':'my pape','shangping':mySpider.deal_name(),'keyword':mySpider.deal_wenben(),'keywords':mySpider.deal_wenben2(),'Specifications':mySpider.deal_wenben5()})#,'Packaging & Delivery':mySpider.deal_wenben4(),'Specifications':mySpider.deal_wenben5()})
