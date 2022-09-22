
public class Kjøretøy {
	
	private String regnr;
	private String fabrikat;
	
	public Kjøretøy(String regnr, String fabrikat) {
		this.regnr = regnr;
		this.fabrikat = fabrikat;
	}

	
	
	public String getRegnr() {
		return regnr;
	}

	public void setRegnr(String regnr) {
		this.regnr = regnr;
	}

	public String getFabrikat() {
		return fabrikat;
	}

	public void setFabrikat(String fabrikat) {
		this.fabrikat = fabrikat;
	}



	@Override
	public String toString() {
		return "Kjøretøy regnr: " + regnr + ", fabrikat: " + fabrikat;
	}
	
	
	
	
	
	

}
