public abstract class Kjoretoy implements Comparable<Kjoretoy>  {
    private String regnr;
    private String produsent;
    private String modell;
    private int regaar;

    public Kjoretoy(String regnr, String produsent, String modell, int regaar) {
        super();
        this.regnr = regnr;
        this.produsent = produsent;
        this.modell = modell;
        this.regaar = regaar;
    }

    public String getRegnr() {
        return regnr;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public String getProdusent() {
        return produsent;
    }

    public void setProdusent(String produsent) {
        this.produsent = produsent;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public int getRegaar() {
        return regaar;
    }

    public void setRegaar(int regaar) {
        this.regaar = regaar;
    }

    @Override
    public String toString() {
        return "Kjoretoy{" +
                "regnr='" + regnr + '\'' +
                ", produsent='" + produsent + '\'' +
                ", modell='" + modell + '\'' +
                ", regaar=" + regaar +
                '}';
    }
    public int compareTo(Kjoretoy denandre) {
        return this.regnr.compareTo(denandre.getRegnr());
    }

    public boolean equals(Kjoretoy denandre) {
        return this.regnr.equals(denandre.getRegnr());
    }
}
