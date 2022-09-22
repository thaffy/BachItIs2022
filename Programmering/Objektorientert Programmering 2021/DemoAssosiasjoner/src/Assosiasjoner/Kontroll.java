package Assosiasjoner;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    // Klassen inneholder 3 datastrukturer:
    private ArrayList<Postadresse> postliste = new ArrayList<>();
    private ArrayList<Person> personliste = new ArrayList<>();
    private ArrayList<Kjoretoy> kjoretoyliste = new ArrayList<>();

    // Metode for å legge til en postadresse:
    // Får verdiene av postnr og poststed
    public void nyPostadresse (String postnr, String poststed) {
        postliste.add(new Postadresse(postnr, poststed));
    }

    public Postadresse finnPostadresse(String postnr) {
        // Bruker linært søk:
        for(int i = 0; i < postliste.size(); i++) {
            Postadresse p = postliste.get(i);
            if (p.getPostnr().equals(postnr)) return p;
        }
        return null;
    }

    public Person finnPerson(String navn) {
        for(int i = 0; i < personliste.size(); i++) {
            Person p = personliste.get(i);
            if (p.getNavn().equals(navn)) return p;
        }
        return null;
    }
    public Kjoretoy finnKjoretoyBinary(String regnr) {
        // Vi må sortere kjøretøyene før binærsøk
        Collections.sort(kjoretoyliste);

        // Binærsøkmetoden skal sammenligne to kjøretøy-objekter
        // Derfor må vi lage et kjøretøy-objekt som inneholder
        // registreringsnummeret vi søker etter:
        Kjoretoy dummy = new Kjoretoy(regnr,null,null);

        // Nå kan vi bruke javas binærsøkmetode:
        // Denne returnerer indeksen til det objektet som har samme regnr som det vi søker etter
        int indeks = Collections.binarySearch(kjoretoyliste,dummy);

        // Hvis et slikt objekt ikke finnes returneres et negativt tall
        // Vi tester derfor på om indeks er større enn eller lik 0.
        if(indeks >= 0) return kjoretoyliste.get(indeks);
        else return null;
    }

    // Metode som legger inn en ny person
    // navn, adresse og postnummer leses inn i grensesnittet
    // og overføres som parametere:
    public void nyPerson(String navn, String adresse, String postnr) {
        // Bruker postnr til å finne en referanse til postadresse objektet
        Postadresse postadresse = finnPostadresse(postnr);
        personliste.add(new Person(navn, adresse,postadresse));
    }
    // Denne metoden skal få et ferdig objekt:
    public void nyttKjoretoy(Kjoretoy kjoretoy) {
        kjoretoyliste.add(kjoretoy);
    }

    public ArrayList<Person> getPersoner() {
        return null;

    }
}
