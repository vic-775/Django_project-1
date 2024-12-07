from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dash-index'),
    path('pred/', views.pred, name='dash-pred')
]