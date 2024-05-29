from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):
    date =datetime.datetime.now()


    d ={'data':'pytHon FuLl StaCk dEvelopmEnT','da':date,'count':'1'}

    return render(request,'filters.html',d)


def userfilters(request):

    d ={'data':'pytHon FuLl StaCk dEvelopmEnT'}

    return render(request, 'userfilters.html',d)