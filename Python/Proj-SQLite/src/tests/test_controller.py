from src.controllers.item_controller import ItemController
from src.models.item import Item

controller = ItemController()
items = controller.pegar_todos_itens()
for item in items:
    print(item)

novo_item = Item("OLA1", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

print("\n**************************************\n")
items = controller.pegar_todos_itens()
for item in items:
    print(item)

print("\n**************************************\n")
item=controller.pegar_item("OLA1")
item.nome="RTX4090"
item.preco = 14999.90
print("Atualiza: ",controller.atualiza_item(item))
print("Remove: ", controller.deleta_item(item))

print("\n**************************************\n")
items = controller.busca_item("Au")
for item in items:
    print(item)