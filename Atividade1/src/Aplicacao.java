public class Aplicacao {
    Usuario u1 = new Usuario("Cleber");

    public static void Alugar(){
        RecursosDeLocomocao v1 = new Carro("cleber");
        v1.testar();
    }

    public static void Trocar(String v){
        if (v == "Moto"){
            RecursosDeLocomocao v1 = new Moto("Cleber");
        } else if (v == "Carro"){
            RecursosDeLocomocao v1 = new Carro("Cleber");
        } else if (v == "Patinete"){
            RecursosDeLocomocao v1 = new Patinete("Cleber");
        } else if (v == "Bicicleta"){
            RecursosDeLocomocao v1 = new Bicicleta("Cleber");
        } else{
            System.out.println("Erro");
        }     
        v1.testar(); 
    }        
}
