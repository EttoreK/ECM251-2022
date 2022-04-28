public class Aplicacao {
    Usuario u1 = new Usuario("Cleber");

    public static void Alugar(){
        RecursosDeLocomocao v1 = new Carro("cleber");
        v1.testar();
    }

    public static void Trocar(String v){
        RecursosDeLocomocao v1 = new RecursosDeLocomocao("cleber");
        if (v == "Moto"){
            v1 = new Moto("Cleber");
        } else if (v == "Carro"){
            v1 = new Carro("Cleber");
        } else if (v == "Patinete"){
            v1 = new Patinete("Cleber");
        } else if (v == "Bicicleta"){
            v1 = new Bicicleta("Cleber");
        } else if(v == v1.getTipo()){
            System.out.println("Troca não faz sentido");
        } else{
            System.out.println("Erro");
        }     
        v1.testar(); 
    }        
}
