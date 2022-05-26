public class Literatura extends Produto{
	private final String editora;
	private final String autor;
	private final EnumGeneroLiteratura genero;
	private final int paginas;
	
	public Literatura(double preco, int quantidade, String nome, String descricao, String editora, String autor,
			EnumGeneroLiteratura genero, int paginas) {
		super(preco, quantidade, nome, descricao);
		this.editora = editora;
		this.autor = autor;
		this.genero = genero;
		this.paginas = paginas;
	}

	public String getEditora() {
		return editora;
	}

	public String getAutor() {
		return autor;
	}

	public EnumGeneroLiteratura getGenero() {
		return genero;
	}

	public int getPaginas() {
		return paginas;
	}

	@Override
	public double gerarPrecoComDesconto() {
		return getPreco();
	}
}
