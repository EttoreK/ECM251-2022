public class App {
    public static void main(String[] args) throws Exception {
    /*    Ninja jiraya = new Ninja("Jiraya", "Sapo", new String[] {"Corte Vertical", "Corte Horizontal"});
        System.out.println("Treinamneto: " + jiraya.train());
        System.out.println(jiraya);
    */
    /* AcademicStudent naruto = new AcademicStudent("Naruto", "Uzumaki", new String[]{"Clone das Sombras", "Tranformação", "Substituição"});
    System.out.println("Trainamento: " + naruto.train());
    System.out.println("Jogatina: " + naruto.play());
    */

    Genin ninja = new Genin("Nome", "Konoha", new String[]{"Jutsu1", "Jutsu2"}, "Coletar items");
    System.out.println(ninja.goToMission());
    System.out.println(ninja.train());
    }
}