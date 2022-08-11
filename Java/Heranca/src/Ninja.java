import java.util.Arrays;

public class Ninja{
    protected String name;
    protected String family;
    private String[] jutsus;

    public Ninja(String name, String family, String[] jutsus){
        this.name = name;
        this.family = family;
        this.jutsus = jutsus;
    }

    public String train(){
        return String.format("%s está treinando", name);
    }

    @Override
    public String toString() {
        return "Ninja [family=" + family + ", jutsus=" + Arrays.toString(jutsus) + ", name=" + name + "]";
    }

    public String getName() {
        return name;
    }
    
    public String[] getJutsus() {
        return jutsus;
    }
}
