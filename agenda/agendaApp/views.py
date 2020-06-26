from django.shortcuts import render

# Create your views here.

def events(request):
    datas = {
        
    }
    return render(request, 'events.html', datas)



def single_event(request):
    datas = {
        
    }
    return render(request, 'single-event.html', datas)