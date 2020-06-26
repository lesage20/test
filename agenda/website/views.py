from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)

def about(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)

def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)

