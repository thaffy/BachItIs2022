package lenketListeDemo;

public class LenketListe<Type> {
    // Deklarerer starten på en liste som består av noder:
    private Node<Type> hode;

    // Metode for å sette inn først i listen:
    public void settInnFørst(Type objekt) {
        // Alltid sjekke om det er noe i listen:
        if(hode == null) hode = new Node(objekt);
        else {
            // "Husker" første node:
            Node<Type> husk = hode;
            // Lager en ny node:
            hode = new Node(objekt);
            // Setter hode.neste til den opprinnelige første noden:
            hode.setNeste(husk);
        }
    }

    // Metode for å slette første node
    public void slettFørste() {
        if(hode != null) hode = hode.getNeste();
    }

    // Lager en toString() for den lenkede listen:
    public String toString() {
        String tekst = "";
        Node hjelpereferanse = hode;
        while(hjelpereferanse != null) {
            tekst = tekst + hjelpereferanse.getinnhold().toString() + "\n";
            hjelpereferanse = hjelpereferanse.getNeste();
        }
        return tekst;
    }
}
