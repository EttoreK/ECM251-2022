public abstract class Pokemon implements Evoluir{
	private final int numero;
	private final String nome;
	protected Status estado;

	public Pokemon(int numero, String nome, Status estado){
		this.numero = numero;
		this.nome = nome;
		this.estado = estado;
	}

	public int getNumero(){
		return numero;
	}

	public String getNome(){
		return nome;
	}

	protected void setEstado(Status estado) {
		this.estado = estado;
	}
	
	public Status getStatus(){
		return null;
	}

	@Override
	public String toString(){
		return "Pokemon [estado=" + estado + ", nome=" + nome + ", numero=" + numero + "]";
	}

	@Override
	public Status somarStatus(Status estado1, Status estado2){
		Status retorno = new Status(estado1.getVida()+estado2.getVida(), 
									estado1.getAtk()+estado2.getAtk(), 
									estado1.getDef()+estado2.getDef(), 
									estado1.getVel()+estado2.getVel());
		return retorno;
	}
}
