import java.util.concurrent.ThreadLocalRandom;

public class RecursosDeLocomocao{
    private int id;
    protected double custohora;
    protected String tipo;
    protected String usuario;

    public RecursosDeLocomocao(String usuario){
        this.usuario = usuario;
        GeraId();
        Tipo();
        Custohora();
    }

    public int GeraId(){
        return this.id = ThreadLocalRandom.current().nextInt(2,99999);
    }

    public void Custohora(){
        this.custohora = 0.0;
    }

    public void Tipo(){
        this.tipo = "Carro";
    }

    @Override
    public String toString(){
        return "Alugas\nid da operaçao: " + id + "\nUsuario: " + usuario + "\nVeiculo escolhido: " + tipo + "\nCusto por hora: " + custohora;
    }

    public void testar(){
        System.out.println(toString());
    }
}