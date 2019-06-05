from django.urls import path
from . import views

urlpatterns = [
    path('searchPubTransPath/', views.send_get),
]