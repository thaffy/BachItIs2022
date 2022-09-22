
public class Person {
	String navn;
	int alder;
	
	
	// Konstruktør med parametere:
	public Person(String navn, int alder) {
		this.navn = navn;
		this.alder = alder;
	}
	
	// Setter for navn:
	public void setNavn(String nynavn) {
		navn = nynavn; //Parameteren har et annet navn enn attributtet
	}
	
	// Setter for alder:
	public void setAlder(int alder) {
		this.alder = alder; // Samme navn på parameteren som på attributtet
	}
	
	// Getter for navn og alder
	public String getNavn() {
		return navn;
	}
	public int getAlder() {
		return alder;
	}
	
	// toString() er en standard metode i OOP (Objektorientert programmering)
	public String toString() {
		return "******\n" + "Navn: " + navn + ", alder: " + alder + "\n******";
	}

}
