public class Conta{
    //Atributos da classe
    private int numero;
    private double saldo;
    private Cliente cliente;

    //Construtor definido para criar um cliente
    public Conta(Cliente cliente, int numero){
        this.numero = numero;
        this.cliente = cliente;
        saldo = 0;
    }

    //Métodos
    public String visualizarSaldo(){
        return String.format("R$ %.2f", saldo);
    }

    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Número da conta:\t" + numero + "\nSaldo disponível:\t" + visualizarSaldo() + "\nNome de cliente:\t" + cliente.getNome();
    }
}