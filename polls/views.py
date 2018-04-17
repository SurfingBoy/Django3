from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    #return HttpResponse('Hello World.')

    string=u'这是从views发过来的信息'
    List=['html','css','java','python']
    dict={'name':u'王武','age':'17'}
    return render(request, 'index.html',{'dict':dict})

def add(request,a,b):
    # a=request.GET.get('a',0)
    # b=request.GET.get('b',0)
    c=int(a)+int(b)
    return HttpResponse(str(c))
def old_add_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add_new',args=(a,b))
    )