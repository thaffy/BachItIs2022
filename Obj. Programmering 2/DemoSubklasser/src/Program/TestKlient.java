package Program;

import java.util.ArrayList;

public class TestKlient {
    public static void main(String[] args) {
        Filkontroll filkontroll = new Filkontroll();

        // Legger inn noen sensurer:
        filkontroll.nyMuntlig("OBJ2000", "Muntlig", 15.5);
        filkontroll.nySkriftlig("OAD2000", "Skriftlig", 4, 15);
        filkontroll.nyProsjekt("BID3000", "Prosjekt", 8);

        // Skriver ut innholdet i arraylisten:
        ArrayList<Sensur> sensurering = filkontroll.getSensurering();
        for (Sensur s : sensurering) {
            System.out.println(s.toString());
        }
        System.out.println();
        System.out.println("Lagrer på fil");
        System.out.println("Sletter innholdet i Arraylisten");
        filkontroll.tømListe();
        System.out.println("Nå er den tom:");

        sensurering = filkontroll.getSensurering();
        for (Sensur s : sensurering) {
            System.out.println(s.toString());
        }

        System.out.println();
        System.out.println("Leser fra fil");
        System.out.println("Arraylisten er nå full igjen:");

        sensurering = filkontroll.getSensurering();
        for (Sensur s : sensurering) {
            System.out.println(s.toString());
        }


    }

}
