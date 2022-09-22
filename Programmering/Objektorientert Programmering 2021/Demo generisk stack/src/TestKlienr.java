
public class TestKlienr {

	public static void main(String[] args) {
		//Lager et objekt av klassen GeneriskStack
		//som bare skal kunne h�ndtere String:
		GeneriskStack<String> stakken = new GeneriskStack<>();
		//Setter inn noen bynavn:
		stakken.push("Kongsberg");
		stakken.push("Drammen");
		stakken.push("H�nefoss");
		System.out.println("�verst i stakken: " + stakken.peek());
		//Skal skrive ut hele stacken:
		System.out.println("Innholdet i stacken:");
		//Henter en array med innholdet i ArrayList'en:
		Object[] byliste = stakken.toArray();
		//Skriver ut alle byene:
		for(int i = byliste.length - 1; i > -1; i--) {
			System.out.println(byliste[i]);
		}
		//Fjerner �vedrste (siste) objekt:
		System.out.println("Fjerner siste (�verste) by: " + stakken.pop());
		//Henter byliste p� nytt:
		byliste = stakken.toArray();
		//Skriver ut p� nytt:
		System.out.println("Stacken ser n� slik ut:");
		for(int i = byliste.length - 1; i > -1; i--) {
			System.out.println(byliste[i]);
		}
	} //main

	
}


