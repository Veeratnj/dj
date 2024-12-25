from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def views_demo(request):
    return HttpResponse('<h1>hello world</h1>')


def views_dynamic_url_path(request,post_id):
    return HttpResponse(f'<h1>hello world</h1>{post_id}')


def views_dynamic_urla_query(request,):
    # print(request.GET.get('id'))
    return HttpResponse(f'<h1>hello world {request.GET.get('id')}</h1>')


def views_redirect_old(request):
    return redirect('new-url')

def  views_redirect_new(request):
    return HttpResponse('this text is from new url')


def views_index(request):
    return render(request=request,template_name='index.html')