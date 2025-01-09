from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Item


def views_demo(request):
    return HttpResponse('<h1>hello world</h1>')


def views_dynamic_url_path(request,post_id):
    return HttpResponse(f'<h1>hello world</h1>{post_id}')


def views_dynamic_urla_query(request,):
 
    return HttpResponse(f"<h1>hello world {request.GET.get('id')}</h1>")


def views_redirect_old(request):
    return redirect('new-url')

def  views_redirect_new(request):
    return HttpResponse('this text is from new url')


def views_index(request):
    loop_data=[
        {'key1':'v1','key2':'v2','key3':'v3'},
        {'key1':'p1','key2':'p2','key3':'p3'},
        {'key1':'q1','key2':'q1','key3':'q3'},
    ]
    # loop_data=[]
    data={'title':'value from python file. hello how are u ??','line_items':loop_data}
    return render(request=request,template_name='index.html',context=data)

def another_page(request):
    return render(request=request,template_name='another_page.html')

def form_page(request):
    if request.method=='POST':
        print(dir(request))
        print(type(request))
        print(request.POST['id'])
    return render(request=request,template_name='contact.html')

# View to display the initial list of items
def item_list(request):
    items = Item.objects.all()[:10]  # Fetch the first 10 items
    return render(request, 'main/item_list.html', {'items': items})

# View to fetch more items via AJAX (3 items at a time)
def get_more_items(request):
    start = int(request.GET.get('start', 0))  # Get the starting index from the query parameter
    end = start + 3  # Fetch 3 more items
    more_items = Item.objects.all()[start:end]  # Query more items
    item_data = [{'item_name': item.item_name, 'price': item.price, 'avl_qty': item.avl_qty} for item in more_items]
    return JsonResponse({'items': item_data})  # Return the items as JSON
    