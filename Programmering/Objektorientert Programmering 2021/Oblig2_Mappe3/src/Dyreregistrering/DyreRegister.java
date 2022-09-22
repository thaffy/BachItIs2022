package Dyreregistrering;
import java.util.ArrayList;

public class DyreRegister {

    private ArrayList<Gaupe> gaupeListe = new ArrayList<>();
    private ArrayList<Hare> hareListe = new ArrayList<>();

    public void nyGaupe(String id,Double lengde, Double vekt, Double oretust, String dato, String fangstomrade) {
        gaupeListe.add(id,lengde,vekt,oretust,dato,fangstomrade);
    }

}