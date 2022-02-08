package BinærTre;

public class Node {
    // Lager en ikke-generisk node:
    private int verdi;

    // Referanse til barna:
    private Node venstre;
    private Node høyre;

    // Referanse til foreldrenoden:
    private Node forelder;

    // Konstruktør
    public Node(int verdi) {
        super();
        this.verdi = verdi;
    }

    // Konstruktør 2
    public Node(int verdi, Node forelder) {
        this.verdi = verdi;
        this.forelder = forelder;
    }

    // Rekursiv metode for innsetting:
    public void settInn(int nyverdi) {
        // Sjekker om verdi i noden er større enn nyverdi
        // I så fall skal nyverdi settes inn til venstre.
        if (verdi <= nyverdi) {
            // Sjekker om det er noe til venstre:
            if (venstre != null) {
                // Det er allerede noe til venstre og vi kaller settInn på ny:
                venstre.settInn(nyverdi);
            }
            // Hvis det ikke er noe til venstre:
            else {
                venstre = new Node(nyverdi, this);
            }
        }
        // Ny verdi skal til høyre
        else {
            if (høyre != null) {
                høyre.settInn(nyverdi);
            } else {
                høyre = new Node(nyverdi, this);
            }
        }
    }

    // Rekursiv søkemetode:
    public boolean søkVerdi(int søkeverdi) {
        if (verdi == søkeverdi) return true;
        if (verdi > søkeverdi) {
            // Søker til venstre
            if (venstre != null) {
                return venstre.søkVerdi(søkeverdi);
            }
            // Ellers så finnes ikke verdien:
            else return false;

        if (høyre != null) {
            return høyre.søkVerdi(søkeverdi);
        }
        else return false;
    }
    public String toString() {
        String returnstreng ="";
        if (venstre != null) {
            returnstreng = returnstreng + venstre.toString();
        }
        if (høyre != null) {
            returnstreng = returnstreng + høyre.toString();
        }
        return returnstreng;

    }
}

