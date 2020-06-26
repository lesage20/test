from django.shortcuts import render

# Create your views here.

def news(request):
    datas = {
        
    }
    return render(request, 'events-news.html', datas)
