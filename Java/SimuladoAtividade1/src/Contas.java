public class Contas{
    //Atributos da classe
    private int idConta;
    private double saldo;
    private Usuario usuario;

    //Construtor definido para criar um cliente
    public Contas(Usuario usuario, int idConta){
        this.idConta = idConta;
        this.usuario = usuario;
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
    
    public boolean transferirDinheiro(double valor, Contas destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Número da conta:\t" + idConta + "\nSaldo disponível:\t" + visualizarSaldo() + "\nNome de cliente:\t" + usuario.getNome();
    }

    public int getId(){
        return idConta;
    }

    public Usuario getUsuario(){
        return usuario;
    }
}