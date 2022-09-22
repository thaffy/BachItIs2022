public class Faglitteratur extends Litteratur {

    String fag;
    String nivaa;

    public Faglitteratur(String isbnNr,String forfatter,String tittel,String utgivelsesaar,String fag,String nivaa) {
        super(isbnNr,forfatter,tittel,utgivelsesaar);
        this.fag = fag;
        this.nivaa = nivaa;
    }

    @Override
    public String toString() {
        return " - Fagområde: " + fag + " - Nivå: " + nivaa + "\n";
    }
}
