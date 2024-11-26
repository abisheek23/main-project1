from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('cources',views.cources),
    path('view_cou/<cid>',views.view_cource),
    path('contact',views.contact),
    path('smessage',views.sendm),
]
