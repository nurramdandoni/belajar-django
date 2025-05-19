
from django.template import loader

from django.http import HttpResponse

# def about(request):
#     return HttpResponse("Hello world!")

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
