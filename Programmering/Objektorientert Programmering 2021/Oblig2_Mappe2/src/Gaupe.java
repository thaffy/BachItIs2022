import java.util.ArrayList;

public class Gaupe<Gaupe> {
    DyreRegister dyreRegister = new DyreRegister();
    public ArrayList<Gaupe> gaupeListe = new ArrayList();
    public ArrayList<Gaupe> gaupeListeGjenfangst = new ArrayList();

    public Gaupe() {
    }

    public int gaupeListeLengde() {
        int listelengde = gaupeListe.size();
        return listelengde;
    }

    public String gaupeGenererNyID() {
        int listelengde = gaupeListeLengde();
        if (listelengde == 0) {
            String nyGaupeID = "G1";
            return nyGaupeID;
        } else {
            int gaupeID = listelengde / 6 + 1;
            String nyGaupeID = "G" + String.valueOf(gaupeID);
            return nyGaupeID;
        }
    }

    public ArrayList<Gaupe> registrerGaupe(String kjonn, Double lengde, Double vekt, Double oretust, String dato, String fangstomrade) {
        String gaupeID = gaupeGenererNyID();
        gaupeListe.add((Gaupe)gaupeID);
        gaupeListe.add((Gaupe)kjonn);
        gaupeListe.add((Gaupe)lengde);
        gaupeListe.add((Gaupe)vekt);
        gaupeListe.add((Gaupe)oretust);
        gaupeListe.add((Gaupe)dato);
        gaupeListe.add((Gaupe)fangstomrade);
        return gaupeListe;
    }

    public ArrayList<Gaupe> gaupeGjenfangst(String dyreID,Double lengde, Double vekt, Double oretust, String dato, String fangstområde) {
        gaupeListeGjenfangst.add((Gaupe)dyreID);
        gaupeListeGjenfangst.add((Gaupe)lengde);
        gaupeListeGjenfangst.add((Gaupe)vekt);
        gaupeListeGjenfangst.add((Gaupe)oretust);
        gaupeListeGjenfangst.add((Gaupe)dato);
        gaupeListeGjenfangst.add((Gaupe)fangstområde);
        return gaupeListeGjenfangst;
    }

    public String genererGaupeRapport() {
        String gaupeRapport = "";
        int listelengde = gaupeListeLengde();
        int m = 0;

        for(int n = 0; n < listelengde / 6; ++n) {
            for(int k = 0; k < 1; ++k) {
                gaupeRapport = gaupeRapport + "Gaupe " + gaupeListe.get(m) + " - ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 1) + "  -  ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 2) + "cm  -  ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 3) + "kg  -  ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 4) + "cm  -  ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 5) + "  -  ";
                gaupeRapport = gaupeRapport + gaupeListe.get(m + 6) + "\n";
                m += 6;
            }

            m++;
            gaupeRapport = gaupeRapport + "\n";
        }

        return gaupeRapport;
    }
}