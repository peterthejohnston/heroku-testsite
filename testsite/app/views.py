from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(
        request,
        'app/index.html',
        context = RequestContext(request,
        {
            'title': 'Home Page',
        })
    )
