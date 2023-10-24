from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import * 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    products = ['apple', 'banana', 'grapes']
    return render(request, 'index.html', {'products': products})

def all_product(request):
    products = Product.objects.all()
    return render(request, 'products.html',{'products':products})

def product_individual(request, prodid):
    product = Product.objects.get(id=prodid)
    return render(request, 'product_individual.html', {'product':product})

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
class UserLoginView(LoginView):
    template_name='login.html'

def logout_user(request):
    logout(request)
    return redirect("/")

def open_view(request):
    return render(request, 'login.html')

@login_required
def locked_view(request):
	return render(request, 'user_signup.html')