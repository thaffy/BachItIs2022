package Assosiasjoner;

public class Postadresse implements Comparable<Postadresse> {
    private String postnr;
    private String poststed;

    public Postadresse(String postnr, String poststed) {
        super();
        this.postnr = postnr;
        this.poststed = poststed;
    }

    public String getPostnr() {
        return postnr;
    }

    public void setPostnr(String postnr) {
        this.postnr = postnr;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    @Override
    public String toString() {
        return "Postadresse{" +
                "postnr='" + postnr + '\'' +
                ", poststed='" + poststed + '\'' +
                '}';
    }

    @Override
    public int compareTo(Postadresse denandre) {
        return this.postnr.compareTo(denandre.getPostnr());
    }
}
