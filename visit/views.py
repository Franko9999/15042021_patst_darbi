from django.shortcuts import render
from visit.models import Visit

def index(request):

	#lai dabutu pirmos piecus objektus klat liekam
	#visit = Visit.objects.all()[:5]

	visits = Visit.objects.all()

	context = {
		'visits' : visits,
	}

	return render(
		template_name = 'index.html',
		request = request,
		context = context,
	)


def add_visit(request):
	if request.method == "POST":

		visit = Visit(
			name=request.POST['name'],
			date = request.POST['date'],
			reason = request.POST['reason'],

		)

		visit.save()

		context = {
			'name': visit.name,
			'date': visit.date,
			'reason': visit.reason,
		}

		return render(
			template_name = "visit.html",
			request = request,
			context = context,
		)

	return render(
		template_name = "form.html",
		request = request,
	)
