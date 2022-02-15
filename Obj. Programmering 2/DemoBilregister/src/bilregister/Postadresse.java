package bilregister;

import java.text.Collator;

public class Postadresse implements Comparable<Postadresse> {
    private String postnummer;
    private String poststed;

    // Oppretter et Collator-objekt for å kunne sortere på skadinaviske bokstaver
    private final static Collator KOLLATOR = Collator.getInstance();

    public Postadresse(String postnummer, String poststed) {
        this.postnummer = postnummer;
        this.poststed = poststed;
    }

    public String getPostnummer() {
        return postnummer;
    }

    public void setPostnummer(String postnummer) {
        this.postnummer = postnummer;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    @Override
    public int compareTo(Postadresse o) {
        return KOLLATOR.compare(this.getPostnummer(),o.getPostnummer());
    }

    public boolean equals(Postadresse o) {
        return KOLLATOR.equals(this.postnummer,o.getPostnummer());
    }

    public String toFile() {
        return postnummer + "," + poststed;
    }
}
