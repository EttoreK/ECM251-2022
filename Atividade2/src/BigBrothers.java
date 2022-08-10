public class BigBrothers extends Membro{

    public BigBrothers(String usuario, String email){
        super(usuario, email,EnumTipoMembros.BIGBROTHERS);     
    }
    
    @Override
    public void postarMensagem(){
        if(Sistema.getTurno() == EnumTurnos.REGULAR){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!" + "\n");
        } else{
            System.out.println("..." + "\n");
        }
    }    
}
