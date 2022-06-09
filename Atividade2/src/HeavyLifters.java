public class HeavyLifters extends Membro {

    public HeavyLifters(String usuario, String email){
        super(usuario, email, "HeavyLifters");
    }

    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno();
        System.out.println(mensagem + "\n" + assinatura + "\n" );
    }
}
