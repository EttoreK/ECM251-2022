public class Bicicleta extends RecursosDeLocomocao{
    public Bicicleta(String id) {
        super(id);
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