public class ScriptGuys extends Membro{

    public ScriptGuys(String usuario, String email){
        super(usuario, email, EnumTipoMembros.SCRIPTGUYS);
    }
    
    @Override
    public void postarMensagem(){
        if(Sistema.getTurno() == EnumTurnos.REGULAR){
            System.out.println("Prazer em ajudar novos amigos de código!" + "\n");
        } else{
            System.out.println("QU3Ro_S3us_r3curs0s.py" + "\n");
        }
    }
    
}