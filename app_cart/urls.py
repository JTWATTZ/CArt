from django.urls import path
from . import views

urlpatterns = [
    # below two paths point to functions in view and htmls 
    path('', views.home, name = 'home'),
    path('checkout/', views.checkout, name = 'checkout'),
    # below two paths point to functions in views
    path('addtocart/', views.addtocart, name = 'addtocart'),
    path('remove_produce/<int:id>', views.remove_produce, name = "remove_produce"),
    
]