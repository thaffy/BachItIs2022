package Oblig2_Registrering;

public class Gaupe extends Dyr {

    // Denne klassen legger bare til tilleggsinformasjonen for gauper som ikke er til felles for alle dyrene.

    private double oretust;

    public Gaupe(String id, String kjonn, String dato, String fangststed, double lengde, double vekt, double oretust) {
        super(id, kjonn, dato, fangststed, lengde, vekt);
        this.oretust = oretust;
    }

    public double getOretust() {
        return oretust;
    }

    @Override
    public String toString() {
        return super.toString() + oretust + "cm" + "\n" ;
    }
}
