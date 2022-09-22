public class Skjonnlitteratur extends Litteratur {

    String kategori;
    String aldersgruppe;

    public Skjonnlitteratur(String isbnNr, String forfatter, String tittel, String utgivelsesaar, String kategori, String aldersgruppe) {
        super(isbnNr, forfatter, tittel, utgivelsesaar);
        this.kategori = kategori;
        this.aldersgruppe = aldersgruppe;
    }

    @Override
    public String toString() {
        return " - Kategori: "+ kategori + "Anbefalt aldersgruppe: " + aldersgruppe + "\n";
    }
}
