import java.util.ArrayList;

public class GeneriskStack<Type> {
	//Oppretter en ArrayList av Type:
	private ArrayList<Type> stakk = new ArrayList<>();
	
	//Metode for � returnere antall objekter:
	public int getSize() {
		//Bruker ArrayList's metode size():
		return stakk.size();
	}
	
	public boolean isEmpty() {
		return stakk.isEmpty();
	}
	
	//Metode for � sette inn et nytt objekt:
	public void push(Type t) {
		//Bruker metoden add() hos ArrayList:
		stakk.add(t);
	}
	
	//Metode for � "se p�" det "�verste" (siste) elementet:
	public Type peek() {
		return stakk.get(stakk.size() - 1);
		
	}
	
	//Metode som henter og fjerner det �verste objektet:
	public Type pop() {
		//Lager en huskereferanse til det siste objektet:
		Type t = stakk.get(stakk.size() - 1);
		//Fjerner objektet fra stacken ved � bruke
		//ArrayList-metoden remove:
		stakk.remove(stakk.size() - 1);
		return t;
	}
	
	//Lager en metode som returnerer innholdet
	//i ArrayList'en som en Object array:
	public Object[] toArray() {
		return stakk.toArray();
	}

}
