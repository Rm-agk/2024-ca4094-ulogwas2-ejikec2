from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.index, name="index"),
   path('home/', views.home, name="homepage"),
   path('products/',views.all_product,name='all_product'),
   path('femaleproducts/',views.all_product,name='female_product'),
   path('products/<int:prodid>/', views.product_individual, name="individual_product"),
   path('femaleproducts/<int:prodid>/', views.female_product_individual, name="female_individual_product" ),
   path('registermale/', views.MaleSignupView.as_view(), name="register"),
   path('registerfemale/', views.FemaleSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('addbasket/<int:prodid>', views.add_to_basket, name="add_basket"),
   path('femaleaddbasket/<int:prodid>', views.female_add_to_basket, name="add_basket"),
   path('basket/', views.show_basket, name="show_basket"),
   path('femalebasket/', views.female_show_basket, name="female_show_basket"),
   path('removeitem/<int:sbi>', views.remove_item, name="remove_basket"),
   path('femaleremoveitem/<int:sbi>', views.femaleremove_item, name="femaleremove_basket"),
   path('order/', views.order, name='order'),
   path('femaleorder/', views.femaleorder, name='femaleorder'),
   path('orderhistory/', views.previous_orders, name="order_history"),
   path('femaleorderhistory/', views.femaleprevious_orders, name="femaleorder_history"),
   path('feedback/', views.feedback_form, name='feedback'),
   path('femalefeedback/', views.femalefeedback_form, name='femalefeedback'),
] 
