from django.urls import path
from . import views  # importand todas las vistas


urlpatterns = [
    path('', views.post_list, name='post_list'), #asociando una vista llamada post_list
]

