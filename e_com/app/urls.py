from django.urls import path
from . import views


urlpatterns = [
    path('',views.e_com_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_com_logout),
    path ('add_prodect',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delet_product/<pid>',views.delet_product)
]
