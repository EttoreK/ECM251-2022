public class Aplicacao{

    public static void Alugar(Usuario u){
        RecursosDeLocomocao v1 = new Carro(u.getNome());
        v1.testar();
    }

    public static void Trocar(Usuario u, String v){
        RecursosDeLocomocao v1 = new RecursosDeLocomocao(u.getNome());
        if (v == "Moto"){
            v1 = new Moto(u.getNome());
        } else if (v == "Carro"){
            v1 = new Carro(u.getNome());
        } else if (v == "Patinete"){
            v1 = new Patinete(u.getNome());
        } else if (v == "Bicicleta"){
            v1 = new Bicicleta(u.getNome());
        } else if(v == v1.getTipo()){
            System.out.println("Troca não faz sentido");
        } else{
            System.out.println("Erro");
            return;
        }     
        v1.testar(); 
    }        
}
