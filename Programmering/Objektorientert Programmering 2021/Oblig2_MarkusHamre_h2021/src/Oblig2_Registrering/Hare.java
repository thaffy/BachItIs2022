package Oblig2_Registrering;

public class Hare extends Dyr {

    // Denne klassen legger bare til tilleggsinformasjonen for harer som ikke er til felles for begge dyrene.

    private String type;
    private String farge;

    public Hare(String id, String kjonn, String dato, String fangststed, double lengde, double vekt, String type, String farge) {
        super(id, kjonn, dato, fangststed, lengde, vekt);
        this.type = type;
        this.farge = farge;
    }

    @Override
    public String toString() {
        return super.toString() + type + "  -  " + farge + "\n";
    }

    public String getType() {
        return type;
    }

    public String getFarge() {
        return farge;
    }
}
