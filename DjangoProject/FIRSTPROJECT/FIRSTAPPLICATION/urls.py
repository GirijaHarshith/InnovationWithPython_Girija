from django.urls import path
from . import views

urlpatterns = [
    path('httpview/', views.firstview, name = 'httpview'),
    path('custom/', views.customwebpage, name = 'Webpage' ),
]