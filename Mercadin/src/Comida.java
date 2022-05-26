public class Comida extends Produto{
	public final EnumTiposComidas tipo;
	public final double peso;
	public final String origem;
	public final EnumAlergias alergias;

	public Comida(double preco, int quantidade, String nome, String descricao, EnumTiposComidas tipo, double peso,
			String origem, EnumAlergias alergias){
		super(preco, quantidade, nome, descricao);
		this.tipo = tipo;
		this.peso = peso;
		this.origem = origem;
		this.alergias = alergias;
	}

	public EnumTiposComidas getTipo(){
		return tipo;
	}

	public double getPeso(){
		return peso;
	}

	public String getOrigem(){
		return origem;
	}

	public EnumAlergias getAlergias(){
		return alergias;
	}

	@Override
	public double gerarPrecoComDesconto() {
		return getPreco() * 0.95;
	}
}
