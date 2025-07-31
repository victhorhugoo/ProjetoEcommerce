from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage, name="homepage"),  # Link, a função e o nome interno desse link
    path('loja/', loja, name="loja"),  
    path('loja/<str:nome_categoria>/', loja, name="loja"), 
    path('produto/<int:id_produto>/', ver_produto, name="ver_produto"), 
    path('produto/<int:id_produto>/<int:id_cor>/', ver_produto, name="ver_produto"), 
    path('minhaconta/', minha_conta, name="minha_conta"),  
    path('login/', login, name="login"),  
    path('carrinho/', carrinho, name="carrinho"),  
    path('checkout/', checkout, name="checkout"),  
    
]