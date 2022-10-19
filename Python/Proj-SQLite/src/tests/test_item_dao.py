from src.dao.item_dao import ItemDAO

itens = ItemDAO.get_instance().get_all()

for item in itens:
	print(item)