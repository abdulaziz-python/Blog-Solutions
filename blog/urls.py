
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
]
