public class App{
    public static void main(String[] args) throws Exception{
        Usuario u1 = new Usuario("Cleber");
        Aplicacao.Alugar(u1);
        Aplicacao.Trocar(u1, "Moto");
        Aplicacao.Trocar(u1, "Patinete");
        Aplicacao.Trocar(u1, "Bicicleta");
        Aplicacao.Trocar(u1, "Bicicleta");
        Aplicacao.Trocar(u1, "Baba");
    }
}