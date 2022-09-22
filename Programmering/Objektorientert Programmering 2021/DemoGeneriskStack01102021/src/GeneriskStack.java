import java.util.ArrayList;

public class GeneriskStack<Type> {
	// Oppretter en ArrayList av Type:
	private ArrayList<Type> stakk = new ArrayList<>();
	
	// Metode for å returnere antall objekter:
	public int getSize() {
		return stakk.size();
	}
	
	public boolean isEmpty() {
		return stakk.isEmpty();
	}
	
	// Implementerer standrdmetodene for en stack:
	// Metoden peek() "ser på" det øverste elementet:
	public Type peek() {
		return stakk.get(stakk.size() - 1);
	}
		
	// Metode for å legge inn nytt element:
	public void push(Type t) {
		stakk.add(t);
	}
	
	// Metode som henter ut og fjerner det siste elementer
	public Type pop() {
		// Vi trenger en "huskereferanse":
		Type t = stakk.get(stakk.size() - 1);
		// Fjerner siste element:
		stakk.remove(stakk.size() - 1);
		return t;
	}
	
}
