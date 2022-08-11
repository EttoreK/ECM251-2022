public class Bicicleta extends RecursosDeLocomocao{
    public Bicicleta(String usuario){
        super(usuario);
    }

    @Override
    public void Custohora(){
        this.custohora = 11.50;
    }

    @Override
    public void Tipo(){
        this.tipo = "Bicicleta";
    }
}