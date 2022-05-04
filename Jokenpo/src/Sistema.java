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
		Jogada jogadas[] = new Jogada[3];
		jogadas[0] = new Pedra();
		jogadas[1] = new Papel();
		jogadas[2] = new Tesoura();
		return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
	}

	private static String avaliaJogadas(Jogada j1, Jogada j2){
		if(j1.verificarVenceu(j2)){
			return "Jogada 1";
		}
		if(j2.verificarVenceu(j1)){
			return "Jogada 2";
		}
		return "Empate";
	}
}