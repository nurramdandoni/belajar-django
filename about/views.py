
from django.template import loader

from django.http import HttpResponse
from .models import About

# def about(request):
#     return HttpResponse("Hello world!")

def about(request):
    template = loader.get_template('about.html')
    dataAbout = About.objects.values()
    context = {
        "about" :dataAbout
    }
    
    print(context)
    
    return HttpResponse(template.render(context,request))
