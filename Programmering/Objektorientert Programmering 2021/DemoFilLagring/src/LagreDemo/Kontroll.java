package LagreDemo;

import hjelpeklasser.*;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Kontroll {
    // Datastruktur
    private ArrayList<Person> personer = new ArrayList<>();

    public void nyPerson(Person person) {
        personer.add(person);
    }

    // Sletter alle verdier i arraylisten
    public void tøm() {
        personer.clear();
    }



    // Metode for å lagre objekter:
    public void skrivData(String filnavn) {
        try {
            // Lager forbindelse til disken:
            PrintWriter utfil = Filbehandling.lagSkriveForbindelse(filnavn);
            // Går gjennom arraylisten:
            for(Person p : personer) {
                utfil.println(p.toFile());
            }
            utfil.close();
        }
        catch (Exception e) {}
    }

    public void lesData(String filnavn) {
        // Tømmer arraylisten
        tøm();

        // Innlesningsblokk
        try {
            // Lager leseforbindelse
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);

            // Leser første linje
            String linje = innfil.readLine();

            // Løkke som går gjennom filen
            while(linje != null) {
                // Splitter ordene per linje basert på komma
                StringTokenizer innhold = new StringTokenizer(linje,",");

                // Leser ordene hver for seg
                String fNavn = innhold.nextToken();
                String eNavn = innhold.nextToken();
                int fÅr = Integer.parseInt(innhold.nextToken());

                // Lager et nytt person objekt med attributtene og legger til i ArrayList-en
                Person pers = new Person(fNavn,eNavn,fÅr);
                personer.add(pers); // Alternativ måte: personer.add(new Person(fNavn,eNavn,fÅr));

                // Leser neste linje
                linje = innfil.readLine();
            }
            innfil.close();
        }
        catch (Exception e) {}
    }

    // Returnerer referanse til ArrayList-en:
    public ArrayList<Person> getPersoner() {
        return personer;
    }
}
