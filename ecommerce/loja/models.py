from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Cliente
        # nome
        # email
        # telefone
        # usuario
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

# Categorias (Masculino, Feminino, Infantil)
        # nome
class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.nome)

# Tipos (Camisa, Camiseta, Bermuda, Calça)
        # nome
class Tipo(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.nome)

# Produto
        # imagem
        # nome
        # preco
        # ativo
        # categoria
        # tipo
class Produto(models.Model):
    imagem = models.CharField(max_length=400, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)
        
# Itemestoque
        # produto (ex.: camisa)
        # cor (ex.: azul, laranja, vermelho)
        # tamanho (ex.: P, M, G)
        # quantidade 
class ItemEstoque(models.Model):
    produto =  models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

# Endereco
        # rua
        # numero
        # complemento
        # cep 
        # cidade 
        # estado 
        # cliente 
class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.IntegerField(default=0)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)


# Pedido
        # cliente
        # data_finalizacao
        # finalizado
        # id_trasacao 
        # endereco 
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transicao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)


# ItensPedido
        # itemestoque (camisa, laranja, M)
        # quantidade (10 itens)
class itensPedido(models.Model):        
    item_estoque =  models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

