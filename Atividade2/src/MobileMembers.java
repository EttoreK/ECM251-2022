public class MobileMembers extends Membro{
    
    public MobileMembers(String usuario, String email) {
        super(usuario, email, "MobileMembers");
        
    }

    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno();
        System.out.println(mensagem + "\n" + assinatura + "\n" );
    }

}