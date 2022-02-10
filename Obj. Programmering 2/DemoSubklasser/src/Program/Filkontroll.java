package Program;

import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Filkontroll {
    private ArrayList<Sensur> sensurering = new ArrayList<>();

    private final String FILNAVN = "sensurering.csv";

    public void nyMuntlig(String fag, String eksamenstype, double lengde) {
        sensurering.add(new MuntligSensur(fag,eksamenstype,lengde));
    }

    public void nySkriftlig(String fag, String eksamenstype, double lengde, int antall) {
        sensurering.add(new SkriftligSensur(fag,eksamenstype,lengde,antall));
    }

    public void nyProsjekt(String fag, String eksamenstype, int antall) {
        sensurering.add(new ProsjektSensur(fag,eksamenstype,antall));
    }

    // Lagrer på fil:
    public void lagre() {
        try {
            // Allokerer fil for skriving
            PrintWriter utfil = Filbehandling.lagSkriveForbindelse(FILNAVN);
            for (Sensur s : sensurering) {
                if(s != null) {utfil.println(s.toFile());}
            }
            utfil.close();
        }
        catch (Exception e) {}
    }

    // Innlesing fra fil:
    public void lese() {
        // Tømmer arraylisten:
        sensurering.clear();
        try {
            BufferedReader innfil = Filbehandling.lagLeseForbindelse(FILNAVN);
            String linje = innfil.readLine();

            // Starter en løkke som går så lenge det er linjer igjen
            while(linje != null) {
                // Lager et StringTokenizer-objekt:
                StringTokenizer innhold = new StringTokenizer(linje,",");

                // Leser sensurtypen:
                String type = innhold.nextToken();

                // Tester på type:
                if(type.equals("M")) lesMuntlig(innhold);
                else if(type.equals("S")) lesSkriftlig(innhold);
                else lesProsjekt(innhold);

                // Leser ny linje
                linje = innfil.readLine();
            }
        }
        catch (Exception e) {}
    }
    private void lesMuntlig(StringTokenizer innhold) {
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        double antallTimer = Double.parseDouble(innhold.nextToken());

        // Legger inn i datastrukturen
        sensurering.add(new MuntligSensur(fag,eksamenstype,antallTimer));
    }

    private void lesSkriftlig(StringTokenizer innhold) {
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        double antallTimer = Double.parseDouble(innhold.nextToken());
        int antallBesvarelser = Integer.parseInt(innhold.nextToken());

        // Legger inn i datastrukturen
        sensurering.add(new SkriftligSensur(fag,eksamenstype,antallTimer,antallBesvarelser));
    }

    private void lesProsjekt(StringTokenizer innhold) {
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        int antall = Integer.parseInt(innhold.nextToken());

        // Legger inn i datastrukturen
        sensurering.add(new ProsjektSensur(fag,eksamenstype,antall));
    }

    public ArrayList<Sensur> getSensurering() {
        return sensurering;
    }

    public void tømListe() {
        sensurering.clear();
    }





}
