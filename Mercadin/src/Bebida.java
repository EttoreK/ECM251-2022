public class Bebida extends Produto{
	public final double volume;
	public final EnumTemperatura temperatura;
	public final EnumTiposBebidas tipo;
	public final EnumAlergias alergias;

	public Bebida(double preco, int quantidade, String nome, String descricao, Double volume,
			EnumTemperatura temperatura, EnumTiposBebidas tipo, EnumAlergias alergias){
		super(preco, quantidade, nome, descricao);
		this.volume = volume;
		this.temperatura = temperatura;
		this.tipo = tipo;
		this.alergias = alergias;
	}

	public double getVolume(){
		return volume;
	}

	public EnumTemperatura getTemperatura(){
		return temperatura;
	}

	public EnumTiposBebidas getTipo(){
		return tipo;
	}

	public EnumAlergias getAlergias(){
		return alergias;
	}

	@Override
	public double gerarPrecoComDesconto(){
		return getPreco() * 0.9;
	}
}
