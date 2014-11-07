from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from competitions.models import Competition


def scoreboard(request):
    # top 20
    data = {
        'top_20': User.objects.all()[:20],
        'more_than_20': User.objects.all().count() > 20
    }
    return render_to_response('competitions/scoreboard.html', data, RequestContext(request))


def competitions(request):
    data = {
        'comps': Competition.objects.all(),
    }
    return render_to_response('competitions/competitions.html', data, RequestContext(request))


def competition(request, slug):
    comp = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=slug)
    assert isinstance(comp, Competition)
    challenges = comp.challenges.all()
    data = {
        'comp': comp,
        'challenges': challenges

    }
    return render_to_response('competitions/competition.html', data, RequestContext(request))