
from django.urls import path
from defUserModelprojapp import views

urlpatterns = [
    path('', views.register , name = 'register'),
    path('login',views.user_login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('logout', views.user_logout, name = 'logout'),
    path('profile', views.user_profile , name = 'profile'),
    path('update', views.update,name = 'update'),
    path('vendor', views.vendor_reg, name = 'vendor'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('foodmenu',views.foodmenu, name = 'foodmenu' ),

    path('restaurant/<int:id>/',views.res_details,name='restaurant_details'),

    path('add-to-cart/<int:id>/',views.add_to_cart,name='add_to_cart'),

    path('cart/',views.cart,name='cart'),
    path('cart/decrease/<int:id>/', views.inc_dec_quantity, name='inc_dec_quantity'),
    path('food/<int:id>/',views.food_details,name='food_details'),
]
