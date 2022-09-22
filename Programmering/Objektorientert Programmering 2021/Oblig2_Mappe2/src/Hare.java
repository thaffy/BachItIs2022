import java.util.ArrayList;

public class Hare<Hare> {

    DyreRegister dyreRegister = new DyreRegister();

    public ArrayList<Hare> hareListe = new ArrayList<>();
    public ArrayList<Hare> hareListeGjenfangst = new ArrayList<>();

    public int hareListeLengde() {
        int listelengde = hareListe.size();
        return listelengde;
    }

    public String hareGenererNyID() {
        int listelengde = hareListeLengde();
        if (listelengde == 0) {
            String nyHareID = "H1";
            return nyHareID;
        } else {
            int hareID = (listelengde / 7) + 1;
            String nyHareID = "H" + String.valueOf(hareID);
            return nyHareID;
        }
    }

    public ArrayList<Hare> registrerHare(String kjonn, Double lengde, Double vekt, String type,String farge, String dato, String fangstomrade) {
        String hareID = hareGenererNyID();
        hareListe.add((Hare) hareID);
        hareListe.add((Hare) kjonn);
        hareListe.add((Hare) lengde);
        hareListe.add((Hare) vekt);
        hareListe.add((Hare) type);
        hareListe.add((Hare) farge);
        hareListe.add((Hare) dato);
        hareListe.add((Hare) fangstomrade);
        return hareListe;
    }

    public ArrayList<Hare> hareGjenfangst(String dyreID,Double lengde, Double vekt,String farge, String dato, String fangstomrade) {
        hareListeGjenfangst.add((Hare)dyreID);
        hareListeGjenfangst.add((Hare)lengde);
        hareListeGjenfangst.add((Hare)vekt);
        hareListeGjenfangst.add((Hare)farge);
        hareListeGjenfangst.add((Hare)dato);
        hareListeGjenfangst.add((Hare)fangstomrade);
        return hareListeGjenfangst;
    }

    public String genererHareRapport() {
        String hareRapport = "";
        int listelengde = hareListeLengde();
        int m = 0;

        // Ytre løkke for alle harer i listen.
        for (int n = 0; n < (listelengde / 7); n++) {
            // Indre løkke for all informasjon per "post".
            for (int k = 0; k < 1; k++) {
                hareRapport += "Hare " + hareListe.get(m) + " - ";
                hareRapport += hareListe.get(m + 1) + "  -  ";
                hareRapport += hareListe.get(m + 2) + "cm  -  ";
                hareRapport += hareListe.get(m + 3) + "kg  -  ";
                hareRapport += hareListe.get(m + 4) + "cm  -  ";
                hareRapport += hareListe.get(m + 5) + "  -  ";
                hareRapport += hareListe.get(m + 6) + "  -  ";
                hareRapport += hareListe.get(m + 7) + "\n";
                m += 7;
            }
            m++;
            hareRapport += "\n";
        }
        return hareRapport;
    }
}


