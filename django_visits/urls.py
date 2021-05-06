"""django_visits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import visit.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visit.views.VisitListView.as_view(), name = 'visit-list'),
    path('visit/<int:pk>', visit.views.VisitDetailView.as_view(), name = 'visit-detail'),
    path('add_visit', visit.views.AddVisitView.as_view()),
    path('filter_by_date', visit.views.FilterByDateView.as_view()),
    path('filter_by_room', visit.views.FilterByRoomView.as_view()),
]
