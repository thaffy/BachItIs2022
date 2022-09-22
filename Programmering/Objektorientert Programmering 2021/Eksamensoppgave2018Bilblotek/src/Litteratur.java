public abstract class Litteratur {

    String isbnNr;
    String forfatter;
    String tittel;
    String utgivelsesaar;

    public Litteratur(String isbnNr, String forfatter, String tittel, String utgivelsesaar) {
        this.isbnNr = isbnNr;
        this.forfatter = forfatter;
        this.tittel = tittel;
        this.utgivelsesaar = utgivelsesaar;
    }

    @Override
    public String toString() {
        return "ISBN nr: " + isbnNr + " - Forfatter: " + forfatter + " - Tittel: " + tittel + " - Utgivelsår: " + utgivelsesaar;
    }


}
