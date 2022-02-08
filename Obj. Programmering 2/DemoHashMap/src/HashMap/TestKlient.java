package HashMap;

import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;

public class TestKlient {

    public static void main(String[] args) {
        // Oppretter en HashMap:
        HashMap<String, Person> hashtabell = new HashMap<>();
        // TreeMap<String, Person> hashtabell = new TreeMap<>();  <--- Tilsvarende med treemap. Har innebygget sortering

        // Oppretter en person:
        String navn = "Ole";
        Person person = new Person(navn,"Vei 1");
        // Legger inn i hashtabellen:
        hashtabell.put(navn,person);

        // Legger til en person til, med mer direkte metode:
        navn = "Lise";
        hashtabell.put(navn, new Person(navn,"Vei 3"));

        // Lister ut innholdet:
        Collection<Person> verdier = hashtabell.values();
        Iterator<Person> oppramser = verdier.iterator();

        // Går gjennom iteratoren:
        while(oppramser.hasNext()) {
            System.out.println(oppramser.next().toString());
        }

    }
}
