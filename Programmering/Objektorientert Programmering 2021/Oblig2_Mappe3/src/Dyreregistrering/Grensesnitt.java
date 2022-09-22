package Dyreregistrering;

import javax.swing.*;

public class Grensesnitt {

    Gaupe gaupe = new Gaupe();
    Hare hare = new Hare();
    DyreRegister dyreRegister = new DyreRegister();

    private final String[] HOVEDMENY = {"Registrer Nytt Dyr","Registrer Gjenfangst","Søk etter dyr","Generer Rapport","Avslutt"};
    private final String[] REGISTRERMENY = {"Registrer Dyreregistrering.Gaupe","Registrer Dyreregistrering.Hare","Tilbake"};

    public int hovedmenyValg() {
        int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
        return valg;
    }

    public int registrermenyValg() {
        int registrerValg = JOptionPane.showOptionDialog(null,"Velg dyretype","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,REGISTRERMENY,REGISTRERMENY[0]);
        return registrerValg;
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
                case 2 : dyreSok();
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

    public void registrerGaupe() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn: ");
        Double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
        Double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
        Double oretust = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde på øretuster: "));
        String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
        String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");

        dyreRegister.nyGaupe(kjonn,lengde,vekt,oretust,dato,fangstomrade);
    }

    public void registrerHare() {
        String kjonn = JOptionPane.showInputDialog("Oppgi kjønn: ");
        Double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
        Double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
        String type = JOptionPane.showInputDialog("Oppgi type hare: ");
        String farge = JOptionPane.showInputDialog("Oppgi harens pelsfarge: ");
        String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
        String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");

        hare.registrerHare(kjonn,lengde,vekt,type,farge,dato,fangstomrade);
    }

    public void gjenfangstDyr() {

        // Finner ut av dyrets type basert på første bokstav i ID'en
        String dyreID = JOptionPane.showInputDialog("Oppgi dyrets ID: ");
        char idBokstav = dyreID.charAt(0);
        String dyreType = Character.toString(idBokstav);

        if (dyreType.equals("G") || dyreType.equals("g")) {
            Double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
            Double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
            Double oretust = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde på øretuster: "));
            String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
            String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
            gaupe.gaupeGjenfangst(dyreID,lengde,vekt,oretust,dato,fangstomrade);
        }
        else {
            Double lengde = Double.valueOf(JOptionPane.showInputDialog("Oppgi lengde: "));
            Double vekt = Double.valueOf(JOptionPane.showInputDialog("Oppgi vekt: "));
            String farge = JOptionPane.showInputDialog("Oppgi harens pelsfarge: ");
            String dato = JOptionPane.showInputDialog("Oppgi fangstdato: ");
            String fangstomrade = JOptionPane.showInputDialog("Oppgi fangstområde: ");
            hare.hareGjenfangst(dyreID,lengde,vekt,farge,dato,fangstomrade);

        }
    }

    public void dyreSok() {
    }

    public void rapportDyr() {
        //String gaupeRapport = gaupe.genererGaupeRapport();
        //String hareRapport = hare.genererHareRapport();
        //JOptionPane.showMessageDialog(null,gaupeRapport);
        //JOptionPane.showMessageDialog(null,hareRapport);
        //System.out.println(gaupeRapport);

    }



}
