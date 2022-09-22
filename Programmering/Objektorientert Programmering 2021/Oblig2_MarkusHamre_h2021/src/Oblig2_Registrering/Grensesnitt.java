package Oblig2_Registrering;

import javax.swing.*;
import java.util.ArrayList;

public class Grensesnitt {
    Kontroll kontroll = new Kontroll();

    private final String[] HOVEDMENY = {"Registrer Nytt Dyr","Registrer Gjenfangst","Søk etter dyr","Generer Rapport","Avslutt"};
    private final String[] REGISTRERMENY = {"Registrer Gaupe","Registrer Hare","Tilbake"};
    private final String[] RAPPORTMENY = {"Full Rapport","Alle Gauper","Alle Harer","Tilbake"};
    private final String[] DYRESOKMENY = {"Linært Søk","Binært Søk","Tilbake"};

    public int hovedmenyValg() {
        int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
        return valg;
    }

    public int registrermenyValg() {
        int registrerValg = JOptionPane.showOptionDialog(null,"Velg dyretype","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,REGISTRERMENY,REGISTRERMENY[0]);
        return registrerValg;
    }

    public int rapportmenyValg() {
        int rapportValg = JOptionPane.showOptionDialog(null,"Velg rapport","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,RAPPORTMENY,RAPPORTMENY[0]);
        return rapportValg;
    }

    public int dyresokValg() {
        int dyresokValg = JOptionPane.showOptionDialog(null,"Velg søkemetode","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,DYRESOKMENY,DYRESOKMENY[0]);
        return dyresokValg;
    }
    // Hovedmeny med henvising til alle funksjonene i programmet.
    public void hovedmeny() {
        boolean fortsett = true;
        while(fortsett) {
            int valg = hovedmenyValg();
            switch(valg) {
                case 0 : registrerDyr();
                    break;
                case 1 : gjenfangstDyr();
                    break;
                case 2 : dyreSokMeny();
                    break;
                case 3 : rapportDyr();
                    break;
                default : fortsett = false;
            }
        }
    }
    // Submeny for registrering av dyr.
    public void registrerDyr() {
        boolean fortsett = true;
        while(fortsett) {
            int valg = registrermenyValg();
            switch (valg) {
                case 0 : registrerGaupe();
                    break;
                case 1 : registrerHare();
                    break;
                default : fortsett = false;
            }
        }
    }
    // Submeny for å velge mellom linært søk og binært søk.
    public void dyreSokMeny() {
        boolean fortsett = true;
        while(fortsett) {
            int valg = dyresokValg();
            switch (valg) {
                case 0 : finnDyrLinear();
                    break;
                case 1 : finnDyrBinary();
                    break;
                default : fortsett = false;
            }
        }
    }

    //
    // Start på alle programfunksjoner
    //

    public void registrerGaupe() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn: ");
        String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
        String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
        double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
        double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
        double oretust = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde på øretuster: "));

        kontroll.registrerGaupe(kjonn,dato,fangstomrade,lengde,vekt,oretust);
    }

    public void registrerHare() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn: ");
        String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
        String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
        double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
        double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
        String type = JOptionPane.showInputDialog("Oppgi type hare: ");
        String farge = JOptionPane.showInputDialog("Oppgi harens pelsfarge: ");

        kontroll.registrerHare(kjonn,dato,fangstomrade,lengde,vekt,type,farge);
    }

    public void gjenfangstDyr() {
        // Finner ut av dyrets type basert på første bokstav i ID'en
        String dyreID = JOptionPane.showInputDialog("Oppgi dyrets ID: ");
        char idBokstav = dyreID.charAt(0);
        String dyreType = Character.toString(idBokstav);

        if (dyreType.equals("G") || dyreType.equals("g")) {
            String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
            String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
            double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
            double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
            double oretust = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde på øretuster: "));

            kontroll.regGaupeGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,oretust);
        }
        else {
            String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
            String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
            double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
            double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
            String farge = JOptionPane.showInputDialog("Oppgi harens pelsfarge: ");

            kontroll.regHareGjenfangst(dyreID,dato,fangstomrade,lengde,vekt,farge);
        }
    }

    public void finnDyrLinear() {
        String dyreID = JOptionPane.showInputDialog("Oppgi dyrets ID: ");
        if(kontroll.isEmpty()) {
            JOptionPane.showMessageDialog(null,"Ingen dyr er registrert.");
        }
        else {
            Dyr indeks = kontroll.finnDyr(dyreID);
            if(indeks == null) {
                JOptionPane.showMessageDialog(null,"Dyret eksisterer ikke.");
            } else {
                ArrayList<Dyr> dyreListe = kontroll.getDyreListe();
                String resultat = "";

                //resultat += indeks.toString();
                //for(Gjenfangst x : dyreListe.get(indexOf(indeks)) {
                //}
                JOptionPane.showMessageDialog(null,resultat);
            }
        }
    }

    public void finnDyrBinary() {
        String dyreID = JOptionPane.showInputDialog("Oppgi dyrets ID: ");
        if(kontroll.isEmpty()) {
            JOptionPane.showMessageDialog(null,"Ingen dyr er registrert.");
        }
        else {
            Dyr indeks = kontroll.finnDyrBinary(dyreID);
            if(indeks == null) {
                JOptionPane.showMessageDialog(null,"Dyret eksisterer ikke.");
            } else JOptionPane.showMessageDialog(null,indeks.toString());
        }
    }


    public void rapportDyr() {
        ArrayList<Dyr> dyreListe = kontroll.getDyreListe();
        String rapport = "";
        for(int i = 0; i < dyreListe.size();i++) {
            Dyr dyr = dyreListe.get(i);
            rapport += dyr.toString();
            for(Gjenfangst x : dyr.getGjenfangstListe()) {
                rapport += x.toString();
            }

        }
        JOptionPane.showMessageDialog(null,rapport);
    }

    // Dette funket ikke, men tanken var at de skulle kunne sammenligne på en eller annen måte, men siden den sammenligner
    // type dyr med type gjenfangst så gikk det skeis!

    /*public void rapportDyr() {
        ArrayList<Dyr> dyreListe = kontroll.getDyreListe();
        ArrayList<Gjenfangst> gaupeGjenfangstListe = kontroll.getGaupeGjenfangst();
        ArrayList<Gjenfangst> hareGjenfangstListe = kontroll.getHareGjenfangst();
        String rapport = "";
        for(int i = 0; i < dyreListe.size();i++) {
            Dyr dyr = dyreListe.get(i);
            rapport += dyr.toString();
            int x;
            for(int j = 0; j<gaupeGjenfangstListe.size(); j++){
                if(dyreListe.contains(gaupeGjenfangstListe.get(j))) {
                    x = j;
                    Gjenfangst gjenfangst = gaupeGjenfangstListe.get(x);
                    rapport += gjenfangst.toString();
                    break;
                }
            }
        }
        JOptionPane.showMessageDialog(null,rapport);
    }*/



}
