package Assosiasjoner;

import java.util.ArrayList;

public class Person implements Comparable<Person> {
    private String navn;
    private String adresse;
    // referanse til Postadresse:
    private Postadresse postadresse;
    // referanse til personens kjøretøyer:
    ArrayList<Kjoretoy> kjoretoyer = new ArrayList<>();

    public Person(String navn, String adresse, Postadresse postadresse) {
        super();
        this.navn = navn;
        this.adresse = adresse;
        this.postadresse = postadresse;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public void setPostadresse(Postadresse postadresse) {
        this.postadresse = postadresse;
    }

    public ArrayList<Kjoretoy> getKjoretoyer() {
        return kjoretoyer;
    }

    public void nyttKjoretoy(Kjoretoy kjoretoy) {
        kjoretoyer.add(kjoretoy);
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", postadresse=" + postadresse +
                '}';
    }

    @Override
    public int compareTo(Person denandre) {
        return this.navn.compareTo(denandre.getNavn());
    }
}
