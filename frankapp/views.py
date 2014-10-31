from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'frankapp/index.html')

def results(request, actor, role, event, day, time, crew, responsibility):
	return render(request, 'frankapp/results.html')
	#    try:
	#        poll = Poll.objects.get(pk=poll_id)
	#    except Poll.DoesNotExist:
	#        raise Http404
	#    return render(request, 'polls/results.html', {'poll': poll})
