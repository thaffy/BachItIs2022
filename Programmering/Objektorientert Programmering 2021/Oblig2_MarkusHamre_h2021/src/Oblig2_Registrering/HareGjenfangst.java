package Oblig2_Registrering;

public class HareGjenfangst extends Gjenfangst {

    private String farge;

    public HareGjenfangst(String dyreID, String dato, String fangstomrade,double vekt,double lengde,String farge) {
        super(dyreID,dato,fangstomrade,vekt,lengde);
        this.farge = farge;
    }

    @Override
    public String toString() {
        return super.toString() + farge + "\n" ;
    }
}