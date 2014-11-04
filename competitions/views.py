from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from competitions.models import Competition


def competition(request, slug):
    comp = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=slug)
    assert isinstance(comp, Competition)
    challenges = comp.challenges.all()
    data = {
        'comp': comp,
        'challenges': challenges

    }
    return render_to_response('competitions/competition.html', data, RequestContext(request))