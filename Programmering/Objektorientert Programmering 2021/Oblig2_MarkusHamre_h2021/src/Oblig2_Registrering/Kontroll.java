package Oblig2_Registrering;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {

    private ArrayList<Dyr> dyreListe = new ArrayList<>();
    private ArrayList<Dyr> gaupeListe = new ArrayList<>();
    private ArrayList<Dyr> hareListe = new ArrayList<>();

    public ArrayList<Gjenfangst> gaupeGjenfangst = new ArrayList<>();
    public ArrayList<Gjenfangst> hareGjenfangst = new ArrayList<>();

    // Lager en ID basert på om gaupelista er tom.
    public int genGaupeID() {
        int gaupeID;
        if(gaupeListe.isEmpty()) {
            gaupeID = 1;
            return gaupeID;
        }
        else {
            int antallGauper = (gaupeListe.size() / 6);
            gaupeID = antallGauper + 1;
            return gaupeID;
        }
    }

    // Lager en ID basert på om harelista er tom.
    public int genHareID() {
        int hareID;
        if(hareListe.isEmpty()) {
            hareID = 1;
            return hareID;
        }
        else {
            int antallHarer = (hareListe.size() / 6);
            hareID = antallHarer + 1;
            return hareID;
        }
    }

    // Legger inn nye gauper i hovedlista dyreListe samt gaupeListe, som brukes til sjekk senere.
    public void registrerGaupe(String kjonn, String dato, String fangststed, double lengde, double vekt,double oretust) {
        String id = "G" + genGaupeID();
        id.trim();
        Gaupe regGaupe = new Gaupe(id,kjonn,dato,fangststed,lengde,vekt,oretust);
        dyreListe.add(regGaupe);
        gaupeListe.add(regGaupe);
    }

    // Legger inn harer i hovedlista dyreListe samt hareListe, som også brukes til sjekk senere i forhold til ID.
    public void registrerHare(String kjonn,String dato,String fangststed,double lengde,double vekt,String type,String farge) {
        String id = "H" + genHareID();
        id.trim();
        Hare regHare = new Hare(id,kjonn,dato,fangststed,lengde,vekt,type,farge);
        dyreListe.add(regHare);
        hareListe.add(regHare);
    }



    public boolean isEmpty() {
        boolean tomListe = dyreListe.isEmpty();
        return tomListe;
    }

    public Dyr finnDyr(String dyreID) {
        // Linært søk!
        Dyr dyr = null;
        boolean found = false;
        int i = 0;
        while(!found) {
           dyr = dyreListe.get(i);
           if(dyreID.equals(dyr.getID())) {
               found = true;
           } else i++;
        } return dyr;
    }

    public Dyr finnDyrBinary(String dyreID) {
        Collections.sort(dyreListe);
        Dyr dummy = new Dyr(dyreID,null,null,null,0,0);
        int i = Collections.binarySearch(dyreListe,dummy);
        if(i >=0) return dyreListe.get(i);
        else return null;
    }

    // Gjenfangst registreringer
    public void regGaupeGjenfangst(String dyreID,String dato,String fangstomrade,double lengde,double vekt, double oretust) {
        // Funket ikke.. GaupeGjenfangst regGaupeGjenfangst = new GaupeGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,oretust);
        //gaupeGjenfangst.add(regGaupeGjenfangst);

        Gaupe gaupe = (Gaupe)finnDyrBinary(dyreID);
        if(gaupe != null) {
            GaupeGjenfangst gaupeGjenFangst = new GaupeGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,oretust);
            gaupe.regGjenfangst(gaupeGjenFangst);
        }
    }

    public void regHareGjenfangst(String dyreID,String dato,String fangstomrade,double lengde,double vekt,String farge) {
        //HareGjenfangst regHareGjenfangst = new HareGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,farge);
        //hareGjenfangst.add(regHareGjenfangst);

        Hare hare = (Hare)finnDyrBinary(dyreID);
        if(hare != null) {
            HareGjenfangst hareGjenFangst = new HareGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,farge);
            hare.regGjenfangst(hareGjenFangst);
        }
    }

    public ArrayList<Dyr> getDyreListe() {
        return dyreListe;
    }

    public ArrayList<Gjenfangst> getGaupeGjenfangst() {
        return gaupeGjenfangst;
    }

    public ArrayList<Gjenfangst> getHareGjenfangst() {
        return hareGjenfangst;
    }


}
