package Program;

public class ProsjektSensur extends Sensur {
    public final double PROSJEKTSENSUR = 8;
    private int antallBesvarelser;

    public ProsjektSensur(String fag, String eksamenstype, int antallBesvarelser) {
        super(fag, eksamenstype);
        this.antallBesvarelser = antallBesvarelser;
    }

    @Override
    public double beregnTidsforbruk() {
        return antallBesvarelser * 8;
    }

    @Override
    public String toFile() {
        return "P" + "," + super.toFile() + "," + antallBesvarelser;
    }
}
