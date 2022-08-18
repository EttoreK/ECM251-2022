from .loja.produto import Produto
from .loja.carrinho import Carrinho

item1 = Produto(199, 'Dark Souls')
item2 = Produto(
    preco = 199, 
    nome = 'Dark Souls',
    descricao = 'Sofra'
    )

carrinho = Carrinho()

carrinho.adicionar(item = item1)
carrinho.adicionar(item = item2)

print('Tamanho: ', carrinho.get_tamanho())
print('Valor: ', carrinho.get_valor_total())