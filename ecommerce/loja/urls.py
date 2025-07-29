from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage, name='homepage'),  # Link, a função e o nome interno desse link
    path('loja/', loja, name='loja'),  
    path('minhaconta/', minha_conta, name='minha_conta'),  
    path('login/', login, name='login'),  
    path('carrinho/', carrinho, name='carrinho'),  
    path('checkout/', checkout, name='checkout'),  
    
]