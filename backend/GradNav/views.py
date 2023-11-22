from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import * 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    user = request.user
    if user.is_anonymous:
        # If user isn't logged in
        return render(request, 'index.html')

    elif user.is_male:
        # User is male
        return render(request, 'products.html')

    else:
        # User is female or other
        return render(request, 'female_products.html')


from django.shortcuts import render
from .models import Product, FemaleProduct

def index(request):
    user = request.user
    if user.is_anonymous:
        # If user isn't logged in
        return render(request, 'index.html')

    elif user.is_male:
        # User is male
        return render(request, 'products.html')

    else:
        # User is female or other
        return render(request, 'female_products.html')

def all_product(request):
    user = request.user
    if user.is_authenticated:
        if user.is_male:
            # Show products for male users
            products = Product.objects.filter(gender='male')
            template_name = 'products.html'
        else:
            # Show products for female users
            products = FemaleProduct.objects.all()
            template_name = 'female_products.html'
    else:
        # Handle cases where the user is not authenticated
        products = Product.objects.all()
        template_name = 'products.html'

    return render(request, template_name, {'products': products})

def product_individual(request, prodid):
    product = Product.objects.get(id=prodid)
    return render(request, 'product_individual.html', {'product':product})

def female_product_individual(request, prodid):
    product = FemaleProduct.objects.get(id=prodid)
    return render(request, 'female_product_individual.html', {'product':product})

class MaleSignupView(CreateView):
    model = User
    form_class = MaleSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
class FemaleSignupView(CreateView):
    model = User
    form_class = FemaleSignupForm
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
    if request.method == 'POST':
        # Display a message to confirm logout using Django messages framework
        messages.info(request, 'Are you sure you want to log out?')

        # Redirect to the same page or a specific confirmation page
        return redirect('confirm_logout')  # You can create a confirm_logout view

    # Original logout logic remains the same if it's not a POST request
    logout(request)
    return redirect("/")

def open_view(request):
    return render(request, 'login.html')

@login_required
def locked_view(request):
	return render(request, 'user_signup.html')

@login_required
def add_to_basket(request, prodid):
    user = request.user
    # is there a shopping basket for the user 
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        # create a new one
        Basket.objects.create(user_id = user)
        basket = Basket.objects.filter(user_id=user, is_active=True).first()
    # get the product 
    product = Product.objects.get(id=prodid)
    sbi = BasketItem.objects.filter(basket_id=basket, product_id = product).first()
    if sbi is None:
        # there is no basket item for that product 
        # create one 
        sbi = BasketItem(basket_id=basket, product_id = product)
        sbi.save()
    else:
        # a basket item already exists 
        # just add 1 to the quantity
        sbi.quantity = sbi.quantity+1
        sbi.save()
    return redirect("/products")

@login_required
def female_add_to_basket(request, prodid):
    user = request.user
    # is there a shopping basket for the user 
    basket = FemaleBasket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        # create a new one
        FemaleBasket.objects.create(user_id = user)
        basket = FemaleBasket.objects.filter(user_id=user, is_active=True).first()
    # get the product 
    product = FemaleProduct.objects.get(id=prodid)
    sbi = FemaleBasketItem.objects.filter(basket_id=basket, product_id = product).first()
    if sbi is None:
        # there is no basket item for that product 
        # create one 
        sbi = FemaleBasketItem(basket_id=basket, product_id = product)
        sbi.save()
    else:
        # a basket item already exists 
        # just add 1 to the quantity
        sbi.quantity = sbi.quantity+1
        sbi.save()
    return redirect("/femaleproducts")

# views.py
@login_required
def show_basket(request):
    # get the user object
    # does a shopping basket exist ? -> your basket is empty
    # load all shopping basket items
    # display on page 
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        #TODO: Show basket empty
        return render(request, 'basket.html', {'empty':True})
    else:
        sbi = BasketItem.objects.filter(basket_id=basket)
        # is this list empty ? 
        if sbi.exists():
            # normal flow
            return render(request, 'basket.html', {'basket':basket, 'sbi':sbi})
        else:
            return render(request, 'basket.html', {'empty':True})
        
@login_required
def female_show_basket(request):
    # get the user object
    # does a shopping basket exist ? -> your basket is empty
    # load all shopping basket items
    # display on page 
    user = request.user
    basket = FemaleBasket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        #TODO: Show basket empty
        return render(request, 'femalebasket.html', {'empty':True})
    else:
        sbi = FemaleBasketItem.objects.filter(basket_id=basket)
        # is this list empty ? 
        if sbi.exists():
            # normal flow
            return render(request, 'femalebasket.html', {'basket':basket, 'sbi':sbi})
        else:
            return render(request, 'femalebasket.html', {'empty':True})
        
@login_required
def remove_item(request,sbi):
    basketitem = BasketItem.objects.get(id=sbi)
    if basketitem is None:
        return redirect("/basket") # if error redirect to shopping basket
    else:
        if basketitem.quantity > 1:
            basketitem.quantity = basketitem.quantity-1
            basketitem.save() # save our changes to the db
        else:
            basketitem.delete() # delete the basket item
    return redirect("/basket")

@login_required
def order(request):
    # load in all data we need, user, basket, items
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        return redirect("/")
    sbi = BasketItem.objects.filter(basket_id=basket)
    if not sbi.exists(): # if there are no items
        return redirect("/")
    # POST or GET
    if request.method == "POST":
        # check if valid
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = user
            order.basket_id = basket
            total = 0.0
            for item in sbi:
                total += float(item.item_price())
            order.total_price = total
            order.save()
            basket.is_active = False
            basket.save()
            return render(request, 'ordercomplete.html', {'order':order, 'basket':basket, 'sbi':sbi})
        else:
            return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi})
    else:
        # show the form
        form = OrderForm()
        return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi})
    
@login_required
def previous_orders(request):
    user = request.user
    orders = Order.objects.filter(user_id=user)
    return render(request, 'previous_orders.html', {'orders':orders})
    
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})