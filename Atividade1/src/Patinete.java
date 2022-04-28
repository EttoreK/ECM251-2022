public class Patinete extends RecursosDeLocomocao{
    public Patinete(String usuario) {
        super(usuario);
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