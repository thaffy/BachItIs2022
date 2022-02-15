
public class Postadresse implements Comparable<Postadresse>{
	private String postnummer,poststed;
	
	public Postadresse(String pnr,String psted) {
		postnummer = pnr;
		poststed = psted;
	}	
	
	public String toString() {
		return postnummer+" "+poststed;
	}
	
	public String getPnr() {
		return this.postnummer;
	}
	
	public int compareTo(Postadresse padr) {
		return this.postnummer.compareTo(padr.getPnr());
	}
	
	public String toFile() {
		return postnummer+","+poststed;
	}
	
}
