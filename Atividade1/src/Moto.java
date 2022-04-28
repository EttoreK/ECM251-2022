public class Moto extends RecursosDeLocomocao{
    public Moto(String id) {
        super(id);
    }

    @Override
    public void Custohora(){
        this.custohora = 26.90;
    }

    @Override
    public void Tipo(){
        this.tipo = "Moto";
    }
}