public class PokemonGrama extends Pokemon{

	public PokemonGrama(int numero, String nome, Status estado){
		super(numero, nome, estado);
	}

	@Override
	public boolean evoluir(Status estado){
		if(estado == null){
			return false;
		}

		Status atual = super.getStatus();
		atual = super.somarStatus(atual, estado);
		atual = super.somarStatus(atual, new Status(20, 10, 10, 20));

		return true;
	}
}
