import java.util.*;
public class Person implements Comparable<Postadresse>{
	String enavn,fnavn;
	Postadresse padresse;
	ArrayList<Bil> biler = new ArrayList<Bil>();
	
	public Person(String enavn,String fnavn,Postadresse padr) {
		this.enavn = enavn;
		this.fnavn = fnavn;
		this.padresse = padr;
	}
	
	public int compareTo(Postadresse p) {
		String smlPnr = p.getPnr();
		String denne = padresse.getPnr();
		return denne.compareTo(smlPnr);
	}
	
	public void regBil(Bil bil) {
		biler.add(bil);
	}
	
	public String getNavn() {
		return enavn;
	}
	
	public String alleBiler() {
		String bilut = "";
		for(int i = 0;i<biler.size();i++) {
			bilut += biler.get(i).toString();			
			bilut += "\n";
		}
		return bilut;
	}
	
	public String toFile() {
		return enavn+","+fnavn+","+padresse.getPnr();
	}
	
	public String toString() {
		return "Etternavn: "+enavn+"\n"+"Biler: "+"\n"+alleBiler();
	}

}
