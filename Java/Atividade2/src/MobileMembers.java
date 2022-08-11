public class MobileMembers extends Membro{
    
    public MobileMembers(String usuario, String email) {
        super(usuario, email, EnumTipoMembros.MOBILEMAMBERS);
        
    }

    @Override
    public void postarMensagem(){
        if(Sistema.getTurno() == EnumTurnos.REGULAR){
            System.out.println("Happy Coding!" + "\n");
        } else{
            System.out.println("Happy_C0d1ng. Maskers" + "\n");
        }
    }

}