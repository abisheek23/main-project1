from django.urls import path
from . import views


urlpatterns = [
    path('',views.e_com_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_com_logout),
    path ('add_prodect',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delet_product/<pid>',views.delet_product),

    #-----------user-----------
    path('register',views.register),
    path('user_home',views.user_home),
    path('viewpro/<pid>',views.view_pro),
    path('view_cart/<pid>',views.add_to_cart),
    path('viewcart/<pid>',views.view_cart),

]
