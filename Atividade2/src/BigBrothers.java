public class BigBrothers extends Membro{

    public BigBrothers(String usuario, String email) {
        super(usuario, email,"BigBrothers");     
    }
    
    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno();
        System.out.println(mensagem + "\n" + assinatura + "\n");
    }    
}
