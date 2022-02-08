package Program;

public abstract class Sensur {
    public final int FORBEREDELSE = 3;
    private String fag;
    private String eksamenstype;

    // Konstruktør
    public Sensur(String fag, String eksamenstype) {
        super();
        this.fag = fag;
        this.eksamenstype = eksamenstype;
    }

    // Get & Set
    public int getFORBEREDELSE() {
        return FORBEREDELSE;
    }

    public String getFag() {
        return fag;
    }

    public void setFag(String fag) {
        this.fag = fag;
    }

    public String getEksamenstype() {
        return eksamenstype;
    }

    public void setEksamenstype(String eksamenstype) {
        this.eksamenstype = eksamenstype;
    }

    // En abstrakt metode for å beregne tidsforbruk:
    public abstract double beregnTidsforbruk();

    // toString():
    @Override
    public String toString() {
        return "Sensur{" +
                "FORBEREDELSE=" + FORBEREDELSE +
                ", fag='" + fag + '\'' +
                ", eksamenstype='" + eksamenstype + '\'' +
                '}';
    }

    // toFile():
    public String toFile() {
        return fag + "," + eksamenstype;
    }
}
