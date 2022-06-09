abstract class Membro implements PostarMensagem{
    private String usuario;
    private String email;
    private String funcao;
    

    public Membro(String usuario, String email, String funcao){
        this.usuario = usuario;
        this.email = email;
        this.funcao = funcao;
    }


    @Override
    public String toString() {
        return "Membro [ usuario = " + usuario + ", email = " + email + ", funcao = " + funcao +"]";
    }
     
    public void mostraHorario(){
        System.out.println(Sistema.getTurno()); 
    }
}
