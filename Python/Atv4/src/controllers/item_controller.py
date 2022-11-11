from src.dao.item_dao import ItemDAO
from src.models.item import Item

class ItemController:
    def __init__(self) -> None:
        pass

    def pegar_item(self, id_prd) -> Item:
        item = ItemDAO.get_instance().pegar_item(id_prd)
        return item

    def inserir_item(self, item) -> bool:
        try:
            ItemDAO.get_instance().inserir_item(item)
        except:
            return False
        return True
    
    def pegar_todos_itens(self) -> list:
        itens = ItemDAO.get_instance().get_all()
        return itens
    
    def atualizar_item(self, item) -> bool:
        return ItemDAO.get_instance().atualizar_item(item)
    
    def deletar_item(self, id_prd) -> bool:
        return ItemDAO.get_instance().deletar_item(id_prd)
    
    def buscar_todos_itens_nome(self, nome) -> list:
        itens = ItemDAO.get_instance().search_all_for_name(nome)
        return itens