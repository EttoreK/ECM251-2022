public class App {
    public static void main(String[] args) throws Exception {
        Cliente c1 = new Cliente("grande", "3242423", "grande@giga", new Conta(1234));
        //c1.setNome("Grande");
        //c1.setCpf("123456759");
        //c1.setEmail("grande@maua.br");
        //c1.setConta(new Conta());
        System.out.println("Nome do cliente: " + c1.getNome());
        System.out.println("E-mail do cliente: " + c1.getEmail());
        System.out.println("CPF do cliente: " + c1.getCpf());
        c1.getConta().visualizarSaldo();
    }
}