package Assosiasjoner;

public class Kjoretoy implements Comparable<Kjoretoy> {
    private String regnr;
    private String modell;
    // Referanse til personen som er eier:
    private Person eier;

    public Kjoretoy(String regnr, String modell, Person eier) {
        this.regnr = regnr;
        this.modell = modell;
        this.eier = eier;
    }

    public String getRegnr() {
        return regnr;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public Person getEier() {
        return eier;
    }

    public void setEier(Person eier) {
        this.eier = eier;
    }

    @Override
    public String toString() {
        return "Kjoretoy{" +
                "regnr='" + regnr + '\'' +
                ", modell='" + modell + '\'' +
                ", eier=" + eier +
                '}';
    }

    @Override
    public int compareTo(Kjoretoy denandre) {
        return this.regnr.compareTo(denandre.getRegnr());
    }
}
