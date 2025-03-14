
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SolutionListView.as_view(), name='solution-list'),
    path('<slug:slug>/', views.SolutionDetailView.as_view(), name='solution-detail'),
]
