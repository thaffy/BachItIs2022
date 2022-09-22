package Oblig2_Registrering;

public class GaupeGjenfangst extends Gjenfangst {

    private double oretust;

    public GaupeGjenfangst(String dyreID, String dato, String fangstomrade,double vekt,double lengde,double oretust) {
        super(dyreID,dato,fangstomrade,vekt,lengde);
        this.oretust = oretust;
    }

    @Override
    public String toString() {
        return super.toString() + oretust + "\n" ;
    }
}
