public class ScriptGuys extends Membro{

    public ScriptGuys(String usuario, String email){
        super(usuario, email, "ScriptGuys");
        
    }
    
    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno();
        System.out.println(mensagem + "\n" + assinatura + "\n");
    }
    
}