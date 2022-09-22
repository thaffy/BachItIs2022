public abstract class Personbil extends Kjoretoy {
    private int antallPlasser;

    public Personbil(String regnr, String produsent, String modell, int regaar) {
        super(regnr, produsent, modell, regaar);
    }

    @Override
    public String toString() {
        return "Personbil{" +
                "antallPlasser=" + antallPlasser +
                "} " + super.toString();
    }
}
