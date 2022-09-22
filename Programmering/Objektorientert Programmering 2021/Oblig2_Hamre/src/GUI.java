import javax.swing.*;

public class GUI {
    private final String[] HOVEDMENY = {"Registrer Nytt Dyr","Registrer Gjenfangst","Søk Etter Dyr","Rapport","Avslutt"};

    private final String[] REGISTERMENY = {"Registrer Gaupe","Registrer Hare","Tilbake"};
    private final String[] GJENFANGST = {""};
    private final String[] DYRESOK = {""};
    private final String[] RAPPORT = {""};

    public int hovedmenyValg() {
        int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Dyreprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
        return valg;
    }

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

    public void registrerDyr() {
        while(true) {
            String gaupeKjonn = JOptionPane.showInputDialog("Kjønn: ");
            String gaupeLengde = JOptionPane.showInputDialog("Lenge: ");
            String gaupeVekt = JOptionPane.showInputDialog("Vekt: ");
            String gaupeEars = JOptionPane.showInputDialog("Lengde på øretuster: ");
            String gaupeDato = JOptionPane.showInputDialog("Dato for fangst: ");

            if (gaupeKjonn == null || gaupeEars == null || gaupeDato == null) break;
        }
    }

    public void gjenfangstDyr() {
    }

    public void dyreSok() {
    }

    public void rapportDyr() {
    }

    public void registrerHare() {
        while(true) {
            String hareKjonn = JOptionPane.showInputDialog("Kjønn: ");
            Double hareLengde = Double.valueOf(JOptionPane.showInputDialog("Lenge: "));
            Double hareVekt = Double.valueOf(JOptionPane.showInputDialog("Vekt: "));
            String hareType = JOptionPane.showInputDialog("Type hare: ");
            String harePels = JOptionPane.showInputDialog("Farge på pels: ");
            String hareDato = JOptionPane.showInputDialog("Dato for fangst: ");

            if (hareKjonn == null) break;
        }
    }



}
