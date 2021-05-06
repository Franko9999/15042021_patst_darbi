from django.shortcuts import render
from django.views.generic import View, ListView
from visit.models import Visit, Room


class AddVisitView(View):
	def get(self, request):
		return render(
			template_name='form.html',
			request=request,
		)

	def post(self, request):
		room_id = request.POST['room_id']
		room = Room.objects.get(id=room_id)

		visit = Visit(
			name=request.POST['name'],
			date=request.POST['date'],
			reason=request.POST['reason'],
			room=room,

		)

		visit.save()

		context = {
			'name': visit.name,
			'date': visit.date,
			'reason': visit.reason,
		}

		return render(
			template_name="visit.html",
			request=request,
			context=context,
		)


class FilterByDateView(View):
	def get(self, request):
		return render(
		template_name='filter_by_date.html',
		request = request,
		)

	def post(self, request):
		date = request.POST['date']

		visits = Visit.objects.filter(date = date)

		context = {
			'visits' : visits,
		}

		return render(
			template_name = 'visit_list.html',
			request = request,
			context = context,
		)


class FilterByRoomView(View):
	def get(self, request):
		return render(
			template_name='filter_by_room.html',
			request=request,
		)

	def post(self, request):
		room_id = request.POST['room_id']
		visits = Visit.objects.filter(room__id=room_id)  # varam ar (room = room), bet
		# tas bus viens lieks query pieprasijums, ar (room__id = room_id)
		#

		context = {
			'visits': visits,
		}

		return render(
			template_name='visit_list.html',
			request=request,
			context=context,
		)

class VisitListView(ListView):
	model = Visit
	template_name = 'visit_list.html'








