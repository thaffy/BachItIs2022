package lenketListeDemo;

public class Node<Type> {

    //Objektet som skal settes inn i den lenkede listen:
    private Type objekt;
    // Referanse til neste node:
    private Node<Type> neste;

    // Konstruktør:
    public Node(Type objekt) {
        this.objekt = objekt;
        neste = null;
    }

    // Metode som returnerer innholdet:
    public Type getinnhold() {
        return objekt;
    }

    // Henter referanse til neste node:
    public Node<Type> getNeste() {
        return neste;
    }

    public void setNeste(Node neste) {
        this.neste = neste;
    }
}
