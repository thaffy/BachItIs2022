
public class MinArray {
	private int lengde = 2;
	private Object[] tabell = new Object[lengde];
	private int antall = 0;
	
	// Metode for å sette inn objekter:
	public void settInn(Object object) {
		// Sjekker om arrayen er full:
		if(antall == tabell.length) {
			utvidTabell();
		}
		tabell[antall] = object;
		antall++;	
	}
	
	// Metode for å lage en ny array.
	// Denne metoden kan godt være private:
	private void utvidTabell() {
		// Lager en ny tabell som er dobbelt så stor
		// som den eksisterende:
		Object[] nyTabell = new Object[lengde*2];
		
		// Kopierer alle objektene fra den gamle til den nye:
		for(int i = 0; i < tabell.length;i++) {
			nyTabell[i] = tabell[i];
		}
		
		// Setter referansen tabell til å refere til nyTabell:
		tabell = nyTabell;
		lengde = tabell.length;
	}
	
	// Metode for å returnere et enkelt objekt:
	public Object getObject(int indeks) {
		return tabell[indeks];
	}
	
	public Object[] getInnhold() {
		return tabell;
	}
	
	// Metode som returnerer størrelsen/antall objekter i tabellen:
	public int getAntall() {
		return antall;
	}
	
	
	

}
