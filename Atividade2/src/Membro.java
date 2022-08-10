abstract class Membro implements PostarMensagem{
    private String usuario;
    private String email;
    
    public Membro(String usuario, String email, EnumTipoMembros nullEnumTipoMembros){
        this.usuario = usuario;
        this.email = email;
    }
}
