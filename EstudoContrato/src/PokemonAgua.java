public class PokemonAgua extends Pokemon{

	public PokemonAgua(int numero, String nome, Status estado){
		super(numero, nome, estado);
	}

	@Override
	public boolean evoluir(Status estado){
		if(estado == null){
			return false;
		}

		Status atual = super.getStatus();
		atual = super.somarStatus(atual, estado);
		atual = super.somarStatus(atual, new Status(0, 0, 10, 0));

		return true;
	}
}
