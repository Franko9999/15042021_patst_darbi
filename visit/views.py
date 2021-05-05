from django.shortcuts import render

def add_visit(request):
	if request.method == "POST":
		name = request.POST['name']
		date = request.POST['date']
		reason = request.POST['reason']

		context = {
			'name': name,
			'date': date,
			'reason': reason,
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
