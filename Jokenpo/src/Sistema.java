import java.util.concurrent.ThreadLocalRandom;

public class Sistema{
	public static void rodar(){
		// Usuário escolhe a jogada
		Jogada jogada1 = new Tesoura();
		// Sorteia 	a jogada do pc
		Jogada jogada2 = sortearJogada();
		// Avaliação das jogadas
		String resultado = avaliaJogadas(jogada1, jogada2);
		// Exibição dos resultados
		System.out.println("Resultado: " + resultado);
	}

	private static Jogada sortearJogada(){
		Jogada jogadas[] = new Jogada[5];
		jogadas[0] = new Pedra();
		jogadas[1] = new Papel();
		jogadas[2] = new Tesoura();
		jogadas[3] = new Spock();
		jogadas[4] = new Lagarto();
		return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
	}

	private static String avaliaJogadas(Jogada j1, Jogada j2){
		System.out.println(j1.toString());
		System.out.println(j2.toString());
		if(j1.verificarVenceu(j2)){
			return "Jogada 1";
		}
		else if(j2.verificarVenceu(j1)){
			return "Jogada 2";
		}
		else{
			return "Empate";
		}
	}
}