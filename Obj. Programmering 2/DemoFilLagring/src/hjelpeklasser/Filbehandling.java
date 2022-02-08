package hjelpeklasser;

import java.io.*;

public class Filbehandling {
    // Metode for å lage en skriveforbindelse:
    public static PrintWriter lagSkriveForbindelse(String filnavn) {
        try {
            FileWriter filforbindelse = new FileWriter(filnavn);
            BufferedWriter skriveBuffer = new BufferedWriter(filforbindelse);
            PrintWriter skriver = new PrintWriter(skriveBuffer);
            return skriver;
        }
        catch (Exception e) {return null;}
    }

    // Metode for leseforbindelse:
    public static BufferedReader lagLeseForbindelse(String filnavn) {
        try {
            FileReader filforbindelse = new FileReader(filnavn);
            BufferedReader leser = new BufferedReader(filforbindelse);
            return leser;
        }
        catch (Exception e) {return null;}
    }
}
