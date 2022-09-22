
public class TestKlienr {

	public static void main(String[] args) {
		//Lager et objekt av klassen GeneriskStack
		//som bare skal kunne håndtere String:
		GeneriskStack<String> stakken = new GeneriskStack<>();
		//Setter inn noen bynavn:
		stakken.push("Kongsberg");
		stakken.push("Drammen");
		stakken.push("Hønefoss");
		System.out.println("Øverst i stakken: " + stakken.peek());
		//Skal skrive ut hele stacken:
		System.out.println("Innholdet i stacken:");
		//Henter en array med innholdet i ArrayList'en:
		Object[] byliste = stakken.toArray();
		//Skriver ut alle byene:
		for(int i = byliste.length - 1; i > -1; i--) {
			System.out.println(byliste[i]);
		}
		//Fjerner øvedrste (siste) objekt:
		System.out.println("Fjerner siste (øverste) by: " + stakken.pop());
		//Henter byliste på nytt:
		byliste = stakken.toArray();
		//Skriver ut på nytt:
		System.out.println("Stacken ser nå slik ut:");
		for(int i = byliste.length - 1; i > -1; i--) {
			System.out.println(byliste[i]);
		}
	} //main

	
}


