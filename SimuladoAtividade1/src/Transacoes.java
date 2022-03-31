public class Transacoes{
    private Contas conta;
    private double valor;
    private String transacao;
    private int aux;

    public Transacoes(Contas conta, double valor){
        aux++ ;
        this.transacao = String.valueOf(aux);
        this.conta = conta;
        this.valor = valor;
    }

    public String Transacao(Contas conta, double valor, String transacao){
        transacao = String.valueOf(conta.getId()) + ";" + String.valueOf(conta.getUsuario()) + ";" + String.valueOf(valor);
        return String.format(transacao);
    }
}