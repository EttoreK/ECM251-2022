import java.util.ArrayList;
import java.util.List;

final class Sistema{
    private static String turno = "Regular";
    private static List<Membro> membros;

    static void run(){
        System.out.println("Bem vindo, Membro!\n");

        membros = new ArrayList<Membro>();
        membros.add(new BigBrothers("", ""));
        membros.add(new HeavyLifters("", ""));
        membros.add(new MobileMembers("", ""));
        membros.add(new ScriptGuys("", ""));

        Sistema.papoDeMembros("");
        
        Sistema.trocarTurno();

        Sistema.papoDeMembros("");

        Sistema.trocarTurno();

        membros.remove(1);
        membros.remove(2);

        Sistema.papoDeMembros("Estou Trabalhando...");

        System.out.println("\nSistema Encerrado...");
    }

    public static String getTurno(){
        return turno;
    }

    public static void setTurno(String turno){
        Sistema.turno = turno;
    }

    public static void trocarTurno(){
        String proximoTurno = Sistema.getTurno();
        Sistema.setTurno(proximoTurno);
        System.out.println(getTurno());
        System.out.println("\n");
    }
    public static void papoDeMembros(String mensagem){
        for(Membro membro : Sistema.membros){
            membro.postarMensagem(mensagem);
        }
    }
}