
public class Poststed {
	private int postnr;
	private String postadresse;
	
	public Poststed(int postnr, String postadresse) {
		super();
		this.postnr = postnr;
		this.postadresse = postadresse;
	}

	public int getPostnr() {
		return postnr;
	}

	public String getPostadresse() {
		return postadresse;
	}
	
	public boolean equlas(Poststed detAndre) {
		return postnr == detAndre.getPostnr();
	}
	
	public String toString() {
		return "postnr: " + postnr + ", postadresse:" + postadresse;
	}
	
	
}
