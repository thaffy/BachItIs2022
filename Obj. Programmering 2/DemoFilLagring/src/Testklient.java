import LagreDemo.Kontroll;
import LagreDemo.Person;

import java.util.ArrayList;

public class Testklient {
    public static void main(String[] args) {
        // Definerer filnavn:
        String filnavn = "personer.csv";
        // Lager et kontrollobjekt:
        Kontroll kontroll = new Kontroll();
        // Legger inn et par personer:
        kontroll.nyPerson(new Person("Ole","Brum",1920));
        kontroll.nyPerson(new Person("Nasse","Nøff",1920));
        kontroll.nyPerson(new Person("Nasséed","Al-Nøff",1920));

        ArrayList<Person> personer = kontroll.getPersoner();
        for(Person p : personer) {
            if(p != null) System.out.println(p.toString());
        }
        kontroll.skrivData(filnavn);
        kontroll.tøm();
        System.out.println("ArrayList'en e nå tom..");

        // Leser inn:
        kontroll.lesData(filnavn);

        for(Person p : personer) {
            if(p != null) System.out.println(p.toString());
        }
    }
}
