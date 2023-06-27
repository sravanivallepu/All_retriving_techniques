from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

from django.http import HttpResponse
def insert_topic(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic data is inserted')

def insert_webpage(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name:')
    u=input('Enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Topic data is inserted')

def insert_accessrecord(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name:')
    u=input('Enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    a=input('enter author:')
    d=input('enter date(yyyy-mm-dd):')
    ARO=Access_Record.objects.get_or_create(author=a,name=WO,date=d)[0]
    ARO.save()
    return HttpResponse('accessrecord data is inserted')


def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='Cricket')
    #LTO=Topic.objects.get(topic_name='Cricket')
    
    d={'LTO':LTO}
    return render(request, 'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.filter(topic_name='Volley Ball')
    LWO=Webpage.objects.exclude(topic_name='Volley Ball')
    LWO=Webpage.objects.all()[3::]
    LWO=Webpage.objects.all()[::-1]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.filter(name__in=['rahul','Dhoni'])
    LWO=Webpage.objects.filter(name__regex='R\w+')
    LWO=Webpage.objects.filter(Q(name='Virat') | Q(url__startswith='https'))
    LWO=Webpage.objects.filter(Q(name='Hardik') & Q(url__startswith='http'))
    
    
    
    d={'LWO':LWO}
    return render(request, 'display_webpages.html',d)

def display_accessrecords(request):
    LARO=Access_Record.objects.all()
    LARO=Access_Record.objects.filter(date='2002-10-06')
    LARO=Access_Record.objects.filter(date__gt='2002-10-06')
   # LARO=Access_Record.objects.filter(date__lte='1995-01-18')
    LARO=Access_Record.objects.filter(date__year='2002')
    #LARO=Access_Record.objects.filter(date__month='07')
    #LARO=Access_Record.objects.filter(date__day='12')
    #LARO=Access_Record.objects.filter(date__year__gte='2020')
    #LARO=Access_Record.objects.filter(date__year__lte='2000')
    #LARO=Access_Record.objects.filter(date__day__gt='12')
    

    d={'LARO':LARO}
    return render(request,'display_accessrecords.html',d)

