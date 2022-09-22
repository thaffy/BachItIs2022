package Dyreregistrering;

public class Gaupe implements Comparable<Gaupe> {

    private Double lengde;
    private Double vekt;
    private Double oretust;
    private String dato;
    private String fangstomrade;



    public Gaupe(Double lengde,Double vekt,Double oretust,String dato,String fangstomrade) {
        this.lengde = lengde;
        this.vekt = vekt;
        this.oretust = oretust;
        this.dato = dato;
        this.fangstomrade = fangstomrade;
    }



    @Override
    public String compareTo(Gaupe denAndre) {
        return this.id.compareTo(denAndre.getID());
    }
}

