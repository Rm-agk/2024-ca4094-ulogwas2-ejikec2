from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.index, name="index"),
   path('', views.index, name="homepage"),
   path('products/',views.all_product,name='all_product'),
   path('products/<int:prodid>/', views.product_individual, name="individual_product" ),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
] 