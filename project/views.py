from django.shortcuts import render

def error(request,exception):
    # print(exception)
    return render(request=request,template_name='custom.html')