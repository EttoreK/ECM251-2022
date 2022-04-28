public class Carro extends RecursosDeLocomocao{
    public Carro(String id) {
        super(id);
    }

    @Override
    public void Custohora(){
        this.custohora = 50.60;
    }

    @Override
    public void Tipo(){
        this.tipo = "Carro";
    }
}
