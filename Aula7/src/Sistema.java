import java.time.LocalDate;
import java.time.Period;

public class Sistema{
    public void run(){
        Cliente cliente = new Cliente("Grande", "99969394", "grande.giga@gmail.com");
        Conta conta = new Conta(cliente, 36925);
        System.out.println(conta);

        Titulo titulo = new Titulo(686.97, LocalDate.of(2022, 3, 30), 5);
    }

    boolean pagarTitulo(Titulo titulo, Conta conta){
        LocalDate prazo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        double valor;
        if(prazo.compareTo(hoje) <= 0){
            valor = titulo.getValor();
        } else{
            valor = titulo.getValor() + titulo.getValor() * (titulo.getMultaDiaria()/100) * Period.between(prazo, hoje).getDays();
        }
        //Pã pã pã, pã pã pãrã...
        return true;
    }
}