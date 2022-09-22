package DyreregisteringOblig2;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll<Dyr> {

    ArrayList<Dyr> dyreListe = new ArrayList<Dyr>();
    ArrayList<Gaupe> gaupeListe = new ArrayList<Gaupe>();
    ArrayList<Hare> hareListe = new ArrayList<Hare>();

    //private int gaupeAntall;
    //private int hareAntall;

    public int getGaupeAntall() {
        int gaupeAntall = (gaupeListe.size() / 6);
        return gaupeAntall;
    }

    public int getHareAntall() {
        int hareAntall = (hareListe.size() / 7);
        return hareAntall;
    }

    public boolean gaupeIsEmpty() {
        boolean gaupeIsEmpty = gaupeListe.isEmpty();
        return gaupeIsEmpty;
    }

    public boolean hareIsEmpty() {
        boolean hareIsEmpty = hareListe.isEmpty();
        return hareIsEmpty;
    }

    public String genererGaupeID() {

        boolean gaupeSjekk = gaupeIsEmpty();
        if(gaupeSjekk) {
            String gaupeID = "G1";
            return gaupeID;
        }
        else {
            String gaupeID = "G" + (getGaupeAntall() + 1);
            return gaupeID;
        }
    }
    public String genererHareID() {
        boolean hareSjekk = hareIsEmpty();
        if(hareSjekk) {
            String hareID = "H1";
            return hareID;
        }
        else {
            String hareID ="H" + (getHareAntall() + 1);
            return hareID;
        }
    }

    public void registrerGaupe(String kjonn,String dato,String fangstomrade,Double vekt, Double lengde, Double oretust) {
        String id = genererGaupeID();
        dyreListe.add((Dyr)id);
        dyreListe.add((Dyr)kjonn);
        dyreListe.add((Dyr)dato);
        dyreListe.add((Dyr)fangstomrade);
        dyreListe.add((Dyr)vekt);
        dyreListe.add((Dyr)lengde);
        dyreListe.add((Dyr)oretust);
    }

    public void registrerHare(String kjonn,String dato,String fangstomrade,Double vekt,Double lengde,String type,String farge) {
        String id = genererHareID();
        dyreListe.add((Dyr)id);
        dyreListe.add((Dyr)kjonn);
        dyreListe.add((Dyr)dato);
        dyreListe.add((Dyr)fangstomrade);
        dyreListe.add((Dyr)vekt);
        dyreListe.add((Dyr)lengde);
        dyreListe.add((Dyr)type);
        dyreListe.add((Dyr)farge);

    }



}
