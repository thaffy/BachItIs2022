package bilregister;

import java.text.Collator;
import java.util.ArrayList;
import java.util.List;

public class Person implements Comparable<Person> {
    private String enavn,fnavn,gateadresse;
    private Postadresse postadresse;
    private final static Collator KOLLATOR = Collator.getInstance();

    // Referanse til bilene en person kan eie:
    private List<Bil> biler = new ArrayList<Bil>();


    public Person(String enavn, String fnavn, String gateadresse, Postadresse postadresse) {
        this.enavn = enavn;
        this.fnavn = fnavn;
        this.gateadresse = gateadresse;
        this.postadresse = postadresse;
    }

    public String getEnavn() {
        return enavn;
    }

    public String getFnavn() {
        return fnavn;
    }

    public String getGateadresse() {
        return gateadresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public List<Bil> getBiler() {
        return biler;
    }

    public void regBil(Bil bil) {
        biler.add(bil);
    }

    public int compareTo(Person person) {
        return KOLLATOR.compare(this.enavn,person.getEnavn());
    }

    @Override
    public String toString() {
        return "Person{" +
                "enavn='" + enavn + '\'' +
                ", fnavn='" + fnavn + '\'' +
                ", gateadresse='" + gateadresse + '\'' +
                ", postadresse=" + postadresse +
                '}';
    }

    public String toFile() {
        return enavn + "," + fnavn + "," + gateadresse + "," + postadresse.getPostnummer();
    }
}
