public class HeavyLifters extends Membro {

    public HeavyLifters(String usuario, String email){
        super(usuario, email, EnumTipoMembros.HEAVYLIFTERS);
    }

    @Override
    public void postarMensagem(){
        if(Sistema.getTurno() == EnumTurnos.REGULAR){
            System.out.println("Podem contar conosco!" + "\n");
        } else{
            System.out.println("N00b_qu3_n_Se_r3pita.bat" + "\n");
        }
    }
}
