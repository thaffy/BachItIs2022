
public class TestKlient {

	public static void main(String[] args) {
		// Lager et objekt av klassen GeneriskStack:
		// Skal bare kunne håndtere String-objekter
		
		GeneriskStack<String> stakken = new GeneriskStack<>();
		// Setter inn noen bynavn:
		stakken.push("Kongsberg");
		stakken.push("Drammen");
		stakken.push("Hønefoss");
		System.out.println("Øverst i stacken: " + stakken.peek());
		
		// Fjerner øverste (siste) objekt:
		String øverst = stakken.pop();
		// Skriver ut hva vi fjernet:
		System.out.println("Vi fjernet " + øverst);
		// Skriver ut hva som nå er øverst:
		System.out.println("Øverste er nå " + stakken.peek());
		

	}

}
