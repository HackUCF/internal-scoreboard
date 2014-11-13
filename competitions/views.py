from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from competitions.forms import AdminSolveForm, SolveForm

from competitions.models import Competition, Challenge


def scoreboard(request):
    # top 20
    data = {
        'top_20': User.objects.all()[:20],
        'more_than_20': User.objects.all().count() > 20
    }
    return render_to_response('competitions/scoreboard.html', data, RequestContext(request))


def challenges(request):
    data = {
        'challenges': Challenge.objects.only('name', 'competition', 'category', 'value', 'solvers').annotate(num_solves=Count('solvers')),
        'show_competition': True
    }
    return render_to_response('competitions/challenges.html', data, RequestContext(request))


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
        'challenges': challenges.annotate(num_solves=Count('solvers'))
    }
    return render_to_response('competitions/competition.html', data, RequestContext(request))


@require_GET
def challenge_ajax(request):
    challenge_id = request.GET.get('id', None)
    try:
        challenge = get_object_or_404(Challenge.objects.prefetch_related('hints'), id=int(challenge_id))
        solved = False
        if challenge.solvers.filter(id=request.user.id).count() == 1:
            solved = True

        data = {
            'challenge': challenge,
            'hints': challenge.hints.all(),
            'solved': solved,
            'num_cols': 4
        }

        form_initial = {'challenge': challenge}
        if request.user.is_superuser:
            data['form'] = AdminSolveForm(initial=form_initial)
        else:
            data['form'] = SolveForm(initial=form_initial)

        return render_to_response('competitions/ajax/challenge.html', data, RequestContext(request))
    except ValueError:
        pass

    return HttpResponseBadRequest()

@require_POST
def challenge_solve_ajax(request):
    if request.user.is_superuser:
        form = AdminSolveForm(request.POST)
    else:
        form = SolveForm(request.POST)

    if form.is_valid():
        challenge = form.cleaned_data['challenge']

        if request.user.is_superuser:
            user = form.cleaned_data['user']
            challenge.solvers.add(user)
            data = {
                'user': user
            }
            return render_to_response('competitions/ajax/admin_solved.html', data, RequestContext(request))
        else:
            return render_to_response('competitions/ajax/solve_submitted.html')

    response = render_to_response('competitions/ajax/challenge.html', {'form': form}, RequestContext(request))
    response.status_code = 400
    return response