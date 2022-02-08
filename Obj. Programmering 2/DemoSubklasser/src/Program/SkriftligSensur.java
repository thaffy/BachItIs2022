package Program;

public class SkriftligSensur extends Sensur {
    public final int GRENSE = 10; // <-- Grensen for når satsen skifter (via faktor1 og faktor2)
    public final double FAKTOR1 = 0.15;
    public final double FAKTOR2 = 0.1;
    private double lengde; // Lengden på eksamen
    private int antallBesvarelser;

    public SkriftligSensur(String fag, String eksamenstype, double lengde, int antallBesvarelser) {
        super(fag, eksamenstype);
        this.lengde = lengde;
        this.antallBesvarelser = antallBesvarelser;
    }

    @Override
    public double beregnTidsforbruk() {
        // Oppretter en variabel som skal returneres:
        double antallTimer = FORBEREDELSE;
        if(antallBesvarelser <= GRENSE) {
            antallTimer += (FAKTOR1 * lengde * antallBesvarelser);
        }
        else {
            antallTimer += ((FAKTOR1 * lengde * GRENSE) + ((antallBesvarelser - GRENSE) * FAKTOR2 * lengde));
        }
        return antallTimer;
    }

    @Override
    public String toFile() {
        return "S" + "," + super.toFile() + "," + lengde + "," + antallBesvarelser;
    }
}
