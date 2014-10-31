from django.shortcuts import render

# Create your views here.
def results(request, actor, role, event, day, time, crew, responsibility):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/results.html', {'poll': poll})
