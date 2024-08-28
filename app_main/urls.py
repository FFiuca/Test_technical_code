from django.urls import path, include
from . import views

app_name='app_main'

urlpatterns = [
    path('segitiga', views.CalculateView.as_view({'post': 'calculate_segitiga'}), name='segitiga'),
    path('ganjil', views.CalculateView.as_view({'post': 'calculate_ganjil'}), name='ganjil'),
    path('prima', views.CalculateView.as_view({'post': 'calculate_prima'}), name='prima'),
]

