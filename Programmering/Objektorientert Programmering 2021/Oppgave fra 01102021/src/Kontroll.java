import java.util.ArrayList;

public class Kontroll {
    // En kontrollklasse skal inneholde datastrukturene
    private ArrayList<Kjoretoy> kjoretoyArrayList = new ArrayList<>();

    // fortutsetter at et objekt av en subklasse av
    // kjoretoy opprettes i grensesnittet (eller testklienten)
    public void nyttKjoretoy(Kjoretoy kjoretoy) {
        kjoretoyArrayList.add(kjoretoy);
    }

    public Kjoretoy finnKjoretoy(String regnr) {
        return null;
    }
}
