from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_GET

from competitions.models import Competition, Challenge


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


@require_GET
def challenge_ajax(request):
    challenge_id = request.GET.get('id', None)
    try:
        challenge = get_object_or_404(Challenge.objects.prefetch_related('hints'), id=int(challenge_id))
        data = {
            'challenge': challenge,
            'hints': challenge.hints.all()
        }
        return render_to_response('competitions/challenge_ajax.html', data)
    except ValueError:
        pass

    return HttpResponseBadRequest()