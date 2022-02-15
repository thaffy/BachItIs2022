package bilregister;

import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Bilregister {
    List<Person> personer = new ArrayList<>();
    List<Bil> biler = new ArrayList<>();
    List<Postadresse> postadresser = new ArrayList<>();

    String bilfil = "biler.csv";
    String personfil = "personer.csv";
    String postadressefil = "postadresser.csv";

    // Søkemetoder
    public Postadresse finnPostadresse(String postnr) {
        for(int i = 0;i < postadresser.size();i++) {
            Postadresse p = postadresser.get(i);
            if(p.getPostnummer().equals(postnr)) return p;
        }
        return null;
    }

    public Person finnPerson(String enavn) {
        for(int j = 0; j < personer.size();j++) {
            Person p = personer.get(j);
            if(p.getEnavn().equals(enavn)) return p;
        }
        return null;
    }

    public Bil finnBil(String regnr) {
        for(int k = 0;k < biler.size();k++) {
            Bil b = biler.get(k);
            if(b.getRegnr().equals(regnr)) return b;
        }
        return null;
    }

    public void skrivPostadresser(String filnavn) throws Exception {
        try {
            PrintWriter utPost = Filbehandling.lagSkriveForbindelse(filnavn);
            for(int i = 0;i < postadresser.size();i++) {
                utPost.println(postadresser.get(i).toFile());
            }
            utPost.close();
        } catch (Exception e) {throw new Exception("Kan ikke skrive til postfil!");}
    }

    public void skrivPersoner(String filnavn) throws Exception {
        try {
            PrintWriter utfil = Filbehandling.lagSkriveForbindelse(filnavn);
            for(int j = 0;j < personer.size(); j++) {
                utfil.println(personer.get(j).toFile());
            }
            utfil.close();
        } catch (Exception e) {throw new Exception("Kan ikke skrive til person-fil!");}
    }

    public void skrivBiler(String filnavn) throws Exception {
        try {
            PrintWriter utfil = Filbehandling.lagSkriveForbindelse(filnavn);
            for(int k = 0; k < biler.size();k++) {
                utfil.println(biler.get(k).toFile());
            }
            utfil.close();
        } catch (Exception e) {throw new Exception("Kan ikke skrive til bil-fil!");}
    }

    public void lesPostadresser(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);

            // Leser første linje...
            String linje = innfil.readLine();

            // Starter løkke
            while(linje!=null) {
                StringTokenizer innhold = new StringTokenizer(linje,",");
                String postnr = innhold.nextToken();
                String poststed = innhold.nextToken();

                Postadresse postadresse = new Postadresse(postnr,poststed);
                postadresser.add(postadresse);

                linje = innfil.readLine();
            }
            innfil.close();
        } catch (Exception e) {throw new Exception("Kan ikke leses fra postadresse-fil :-( ");}
    }

    public void lesPersoner(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);
            String linje = innfil.readLine();
            while(linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje,",");
                String enavn = innhold.nextToken();
                String fnavn = innhold.nextToken();
                String gateadresse = innhold.nextToken();
                String postnr = innhold.nextToken();

                Postadresse postadresse = finnPostadresse(postnr);

                Person person = new Person(enavn,fnavn,gateadresse,postadresse);
                personer.add(person);

                linje = innfil.readLine();
            }
            innfil.close();
        } catch (Exception e) {throw new Exception("Kan ikke leses fra person-fil :-( ");}
    }

    public void lesBiler(String filnavn) throws Exception {
        try {
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(filnavn);
            String linje = innfil.readLine();
            while(linje != null) {
                StringTokenizer innhold = new StringTokenizer(linje,",");
                String regnr = innhold.nextToken();
                String merke = innhold.nextToken();
                String modell = innhold.nextToken();
                String enavn = innhold.nextToken();

                // Finner personobjektet
                Person eier = finnPerson(enavn);

                Bil bil = new Bil(regnr,merke,modell,eier);
                biler.add(bil);

                // Legger bilen inn i eierens bil-arraylist
                eier.regBil(bil);

                linje = innfil.readLine();
            }
            innfil.close();
        } catch (Exception e) {throw new Exception("Kan ikke leses fra bil-fil :-( ");}
    }

    public void lesAlleFiler() throws Exception {
        try {
            lesPostadresser(postadressefil);
            lesPersoner(personfil);
            lesBiler(bilfil);

        } catch (Exception e) {throw e;}
    }

    public void skrivAlleFiler() throws Exception {
        try {
            skrivPostadresser(postadressefil);
            skrivPersoner(personfil);
            skrivBiler(bilfil);
        } catch (Exception e) {throw e;}
    }


    public void regBil(String regnr, String merke, String modell, Person eier) {
        Bil bil = new Bil(regnr,merke,modell,eier);
        biler.add(bil);
    }
}
