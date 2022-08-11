public class Status{
	private int vida;
	private int atk;
	private int def;
	private int vel;
	
	public Status(int vida, int atk, int def, int vel){
		this.vida = vida;
		this.atk = atk;
		this.def = def;
		this.vel = vel;
	}

	public int getVida(){
		return vida;
	}

	public int getAtk(){
		return atk;
	}

	public int getDef(){
		return def;
	}

	public int getVel(){
		return vel;
	}

	@Override
	public String toString() {
		return "Status [atk=" + atk + ", def=" + def + ", vel=" + vel + ", vida=" + vida + "]";
	}
}
