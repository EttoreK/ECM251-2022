public class App{
    public static void main(String[] args) throws Exception{
        Produto manga = new Literatura(29.90, 10, "Gants", "soco soco", "Panini", "Hiroikish Amamoto", EnumGeneroLiteratura.ACAO, 100);
        Produto coca = new Bebida(10.5, 3, "Coca", "Pior que Guaraná", 0.5, EnumTemperatura.FRIO, EnumTiposBebidas.REFRIGERANTE, EnumAlergias.GLUTEM);
        Produto tepoki = new Comida(23.40, 1, "tepoki", "comida coreana do lula", EnumTiposComidas.APIMENTADA, 2.45, "Coreia", EnumAlergias.GLUTEM);

        System.out.println("Preços Regulares:");
        System.out.println(manga.getNome()+": R$ "+manga.getPreco());
        System.out.println(coca.getNome()+": R$ "+coca.getPreco());
        System.out.println(tepoki.getNome()+": R$ "+tepoki.getPreco());

        System.out.println("Preços +Barato:");
        System.out.println(manga.getNome()+": R$ "+precoComDesconto(manga));
        System.out.println(coca.getNome()+": R$ "+precoComDesconto(coca));
        System.out.println(tepoki.getNome()+": R$ "+precoComDesconto(tepoki));
    }

    public static String precoComDesconto(IGerarDesconto produto){
        return "R$ "+produto.gerarPrecoComDesconto();
    }
}
