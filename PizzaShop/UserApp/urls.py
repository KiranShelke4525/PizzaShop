from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login),
    path('signup', views.signup),
    path('signout',views.signout),
    path('menu',views.menu), 
    path('ShowPizzas/<id>',views.ShowPizzas),
    path('about',views.about), 
    path('contact',views.contact), 
    path('services',views.services),
    path('ViewDetails/<id>',views.ViewDetails),
    path('addToCart',views.addToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('removeItem',views.removeItem),
    path('MakePayment',views.MakePayment),
    path('paymentsucces',views.paymentsucces),
   

]