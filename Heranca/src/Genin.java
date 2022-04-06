public class Genin extends Ninja{

    public Genin(String name, String family, String[] jutsus, String mission) {
        super(name, family, jutsus);
        this.mission = mission;    
    }

    private String mission;

    public String goToMission(){
        return String.format("%s esta indo na missao %s", name, mission);
    }

    @Override
    public String train(){
        return String.format("%s está treinando o jutsu %s!", name , getJutsus()[0]);
    }
}