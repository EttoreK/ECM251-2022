public class PokemonFogo extends Pokemon{

	public PokemonFogo(int numero, String nome, Status estado){
		super(numero, nome, estado);
	}

	@Override
	public boolean evoluir(Status estado){
		if(estado == null){
			return false;
		}

		Status atual = super.getStatus();
		atual = super.somarStatus(atual, estado);
		atual = super.somarStatus(atual, new Status(0, 10, 0, 0));

		return true;
	}
}
