from django.shortcuts import render_to_response
from django.template import RequestContext
from competitions.models import Competition


def index(request):
    data = {
        'comps': Competition.objects.all()
    }
    return render_to_response('index.html', data, RequestContext(request))