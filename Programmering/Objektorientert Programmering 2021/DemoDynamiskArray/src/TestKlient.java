
public class TestKlient {

	public static void main(String[] args) {
		MinArray minarray = new MinArray();
		
		// Setter inn String-objekter:
		minarray.settInn("Kaffe");
		minarray.settInn("Fløte");
		
		// Setter inn et tredje ord for å sjekke utvidelsesmetoden...
		minarray.settInn("Kake");
		
		// Finner antall objekter
		int antall = minarray.getAntall();
		System.out.println(antall);
		
		// Skriver ut innholdet:
		for(int i = 0; i < antall;i++) {
			System.out.println(minarray.getObject(i));
		}

	}

}
