public class TestDrive{
    public static void executar(){
        Dado d1 = new Dado("1234");
        System.out.println("Criado Dado Generico: " + d1);
        System.out.println("Face atual: " + d1.faceAtual());
        //Sortear nova Face
        d1.rodar();
        System.out.println("Face atual: " + d1.faceAtual());

        // change mudança

        Dado d2 = new DadoD6("3473");
        System.out.println("Criado Dado D6: " + d2);
        System.out.println("Face atual: " + d2.faceAtual());
        //Sortear nova Face
        d2.rodar();
        System.out.println("Face atual: " + d2.faceAtual());

        Dado d3 = new DadoD10("4358");
        System.out.println("Criado Dado D10: " + d3);
        System.out.println("Face atual: " + d3.faceAtual());
        //Sortear nova Face
        d3.rodar();
        System.out.println("Face atual: " + d3.faceAtual());

        Dado d4 = new DadoD20("2391");
        System.out.println("Criado Dado D20: " + d4);
        System.out.println("Face atual: " + d4.faceAtual());
        //Sortear nova Face
        d4.rodar();
        System.out.println("Face atual: " + d4.faceAtual());
    }
}