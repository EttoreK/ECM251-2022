import java.util.ArrayList;
import java.util.List;

final class Sistema{
    protected static EnumTurnos turno = EnumTurnos.REGULAR;
    private static List<Membro> membros = new ArrayList<Membro>();

    static void run(){
        membros.add(new MobileMembers("C4r1inh0", "C4r1inh0p14y5@yahoo.com.br"));
        membros.add(new HeavyLifters("D3137i", "D3137iD0V4113y@outlook.com"));
        membros.add(new ScriptGuys("C0n7r01", "C0n7r01j0g0d04n0@apple.com"));
        membros.add(new BigBrothers("B1az3", "B1az3@hotmail.com"));

        Sistema.postarMensagem();

        Sistema.trocaTurno();

        Sistema.postarMensagem();

        Sistema.trocaTurno();

        membros.remove(1);
        membros.remove(1);

        Sistema.postarMensagem();

        System.out.println("\nEncerrado o Sistema\n");
    }

    public static void setTurno(EnumTurnos turno){
        Sistema.turno = turno;
    }

    public static void trocaTurno(){
        if(Sistema.turno == EnumTurnos.REGULAR){
            Sistema.turno = EnumTurnos.EXTRA;
        } else{
            Sistema.turno = EnumTurnos.REGULAR;
        }
    }
    public static void postarMensagem(){
        System.out.println("Turno: " + getTurno());
        for(Membro membro : Sistema.membros){
            membro.postarMensagem();
        }
    }

    public static EnumTurnos getTurno(){
        return turno;
    }
}