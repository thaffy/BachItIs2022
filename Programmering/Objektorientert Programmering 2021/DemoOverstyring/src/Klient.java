
public class Klient {

	public static void main(String[] args) {
		Kontroll kontroll = new Kontroll();
		Trailer t = new Trailer("AC12345","MAN",25);
		kontroll.settInn(t);
		// Mer kompakt kode:
		kontroll.settInn(new Kjøretøy("CB23456","Volvo"));
		kontroll.settInn(new Buss("BC23456","Scania",50));
		
		Kjøretøy[] kjøretøy = kontroll.getKjøretøy();
		// Utvidet for-løkke går gjennom og kaller objektenes toString()
		for(Kjøretøy k : kjøretøy) {
			if(k !=null) System.out.println(k.toString());
		}
	}

}
