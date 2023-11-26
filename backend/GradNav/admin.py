from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'GradNav Salon'
admin.site.register(User)
admin.site.register(Product)
admin.site.register(FemaleProduct)
admin.site.register(Basket)
admin.site.register(FemaleBasket)
admin.site.register(BasketItem)
admin.site.register(FemaleBasketItem)
admin.site.register(Order)
admin.site.register(FemaleOrder)
admin.site.register(Feedback)
admin.site.register(FemaleFeedback)

