import java.util.*;
public class Bil implements Comparable<Bil>{
	String regnr,merke;
	Person eier;
	
	public Bil(String regnr,String merke,Person eier) {
		this.regnr = regnr;
		this.merke = merke;
		this.eier = eier;
	}
	
	
	public Person getEier() {
		return eier;		
	}
	
	public String getRegnr() {
		return this.regnr;
	}
	
	public int compareTo(Bil bil) {
		return this.regnr.compareTo(bil.getRegnr());
	}
	
	public String toString() {
		return regnr+" "+merke;
	}
	
	public String toFile() {
		return eier.getNavn()+","+regnr+","+merke;
	}

}
