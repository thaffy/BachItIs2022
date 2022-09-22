import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class DyreRegister<Dyr> implements Comparable<Dyr> {

    public ArrayList<Dyr> komplettRapport = new ArrayList<>();

    public ArrayList<Dyr> komplettRapport(ArrayList<Gaupe> gaupeListe,ArrayList<Hare> hareListe) {
        komplettRapport.addAll((Collection<? extends Dyr>) gaupeListe);
        komplettRapport.addAll((Collection<? extends Dyr>) hareListe);
        return komplettRapport;
    }

    public String genererRapport() {
        String rapport = "";
        return rapport;
    }

    public Dyr finnDyr (String dyreID) {
        Collections.sort(komplettRapport);
    }

    @Override
    public int compareTo(Dyr dyr) {
        return 0;
    }
}
