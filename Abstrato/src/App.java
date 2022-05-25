public class App {
    public static void main(String[] args) throws Exception{
        Configuracao c1;
        Configuracao c2;

        c1 = new ConfiguracaoDesenvolvimento("localhost", "localhost:5000");
        c2 = new ConfiguracaoProducao("http://aws.meubanco.com", "https://minhamaua.br", "Jorge");
        System.out.println("Config: " + c1);
        System.out.println("Config: " + c2);
        
        System.out.println(c1.getUser());
        System.out.println(c2.getUser());
    }
}
