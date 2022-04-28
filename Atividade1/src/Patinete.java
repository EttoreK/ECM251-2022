public class Patinete extends RecursosDeLocomocao{
    public Patinete(String id) {
        super(id);
    }

    @Override
    public void Custohora(){
        this.custohora = 6.00;
    }

    @Override
    public void Tipo(){
        this.tipo = "Patinete";
    }
}