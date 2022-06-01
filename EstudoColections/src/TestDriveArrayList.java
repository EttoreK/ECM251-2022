import java.util.ArrayList;

public class TestDriveArrayList{
	public static void main(String[] args){
		// Cria uma lista para as canetas
		ArrayList<Caneta> canetas = new ArrayList<Caneta>();
		// Adiciona uma caneta
		canetas.add(new Caneta("Azul", 0.7));
		canetas.add(new Caneta("Vermelha", 1));

		// Passar por todos os elementos
		// Método 1
		for(int i = 0; i<canetas.size(); i++){
			System.out.println("Cor da Caneta: "+((Caneta)canetas.get(i)).cor);
		}

		// Método 2
		for(Caneta caneta : canetas){
			System.out.println("Cor da caneta: "+caneta.cor);
		}
	}
}
