package lenketListeDemo;

public class TestKlient {

    public static void main(String[] args) {
        LenketListe<String> lenke = new LenketListe<>();
        lenke.settInnFørst("Arne");
        lenke.settInnFørst("Nemi");
        lenke.settInnFørst("Krille");
        // Skriver ut:
        System.out.println(lenke.toString());
    }
}
