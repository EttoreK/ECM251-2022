abstract class Membro implements PostarMensagem{
    private String usuario;
    private String email;
    private EnumTipoMembros funcao;
    

    public Membro(String usuario, String email, EnumTipoMembros scriptguys){
        this.usuario = usuario;
        this.email = email;
        this.funcao = null;
    }

    @Override
    public String toString() {
        return "Membro [email=" + email + ", funcao=" + funcao + ", usuario=" + usuario + "]";
    }
}
