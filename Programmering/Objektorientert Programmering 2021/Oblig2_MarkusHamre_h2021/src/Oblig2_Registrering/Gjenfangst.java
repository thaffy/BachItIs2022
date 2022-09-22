package Oblig2_Registrering;

public class Gjenfangst {
    private String dyreID;
    private String dato;
    private String fangstomrade;
    private double vekt;
    private double lengde;

    public Gjenfangst(String dyreID, String dato,String fangstomrade, double vekt, double lengde) {
        this.dyreID = dyreID;
        this.dato = dato;
        this.fangstomrade = fangstomrade;
        this.vekt = vekt;
        this.lengde = lengde;
    }

    public String toString() {
        return "--Gjenfangstdato: " + dato + "  -  " + fangstomrade + "  -  " + vekt + "kg  -  " + lengde + "cm  -  ";

    }
}
