from Modelos.documentos import Book, Document, EMail
from Modelos.plantas import Arvore, Alface

def run_system():
	doc1 = Document()
	doc2 = EMail(to='email@sim', authors=["Eu"])
	doc3 = Book(title="Design", authors=["Eric", "John", "Ralph", "Ricardão"])
	
	print(doc2.get_authors())
	print(doc3)

if __name__ == "__main__":
	# planta1 = Arvore('Carvalho')
	# planta2 = Alface(nomes="Hamburguer")

	# print(planta1.ola())
	# print(planta2.ola())
	run_system()