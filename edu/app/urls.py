from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('contact',views.contact),
    path('courses',views.courses),
    path('placement',views.placement),
    path('about',views.about),           
]