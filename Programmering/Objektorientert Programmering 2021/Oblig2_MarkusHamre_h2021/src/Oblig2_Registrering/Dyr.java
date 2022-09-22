package Oblig2_Registrering;

import java.util.ArrayList;

public class Dyr implements Comparable<Dyr> {

    private String id;
    private String kjonn;
    private String dato;
    private String fangststed;
    private double lengde;
    private double vekt;

    private ArrayList<Gjenfangst> gjenfangstListe = new ArrayList<Gjenfangst>();

    public Dyr(String id, String kjonn, String dato, String fangststed, double lengde, double vekt) {
        this.id = id;
        this.kjonn = kjonn;
        this.dato = dato;
        this.fangststed = fangststed;
        this.lengde = lengde;
        this.vekt = vekt;
    }

    public String getID() {
        return id;
    }

    public String toString() {
        return "ID: " + id + "  -  " + kjonn + "  -  " + dato + "  -  " + fangststed + "  -  " + lengde + "cm -  " + vekt + "kg  -  ";
    }

    public void regGjenfangst(Gjenfangst x) {
        gjenfangstListe.add(x);
    }

    public ArrayList<Gjenfangst> getGjenfangstListe() {
        return gjenfangstListe;
    }

    @Override
    public int compareTo(Dyr dyr) {
        return this.id.compareTo(dyr.getID());
    }

    public String getKjonn() {
        return kjonn;
    }

    public String getDato() {
        return dato;
    }

    public String getFangststed() {
        return fangststed;
    }

    public double getLengde() {
        return lengde;
    }

    public double getVekt() {
        return vekt;
    }
}
