public abstract class Produto implements IGerarDesconto{
	private double preco;
	private int quantidade;
	private final String nome;
	private final String descricao;
	
	public Produto(double preco, int quantidade, String nome, String descricao){
		this.preco = preco;
		this.quantidade = quantidade;
		this.nome = nome;
		this.descricao = descricao;
	}

	public double getPreco(){
		return preco;
	}

	public void setPreco(double preco){
		this.preco = preco;
	}

	public int getQuantidade(){
		return quantidade;
	}

	public void setQuantidade(int quantidade){
		this.quantidade = quantidade;
	}

	public String getNome(){
		return nome;
	}

	public String getDescricao(){
		return descricao;
	}
}
