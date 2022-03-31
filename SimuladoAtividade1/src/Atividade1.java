public class Atividade1{
    public void run(){
        Usuario usuario = new Usuario("Grande", "SuperSenha", "grande.giga@gmail.com");
        Contas conta = new Contas(usuario, 36925);
        //System.out.println(conta);

        Transacoes transaco = new Transacoes(conta, 78);
    }
    System.out.println(Transacao(conta, 78, transaco));
}