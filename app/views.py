from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
from app.forms import *

def insert_topic(request):
    TN=TopicForm()
    d={'TN':TN}

    if request.method=='POST':
        TND=TopicForm(request.POST)
        if TND.is_valid():
            TND.save()
            return HttpResponse('Topic data inserted successfully...!')
        else:
            return HttpResponse("inserted data is not valid")
    return render(request,'insert_topic.html',d)