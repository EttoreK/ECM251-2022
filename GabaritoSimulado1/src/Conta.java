public class Conta{
    private int idConta;
    private double saldo;
    private static int totalContas = 0;

    public Conta(){
        this.saldo = 0;
        idConta = totalContas;
        totalContas++;
    }
    public boolean depositar(double valor){
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > this.saldo)
            return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
    }
    @Override
    public String toString() {
        return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
    }
    public int getIdConta() {
        return idConta;
    }
    public double getSaldo() {
        return saldo;
    }
}
