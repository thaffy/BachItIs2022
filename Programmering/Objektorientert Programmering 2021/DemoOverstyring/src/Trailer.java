
public class Trailer extends Kjøretøy {
	
	private int lastevolum;

	public Trailer(String regnr, String fabrikat, int lastevolum) {
		super(regnr, fabrikat);
		this.lastevolum = lastevolum;
	}

	public int getLastevolum() {
		return lastevolum;
	}

	public void setLastevolum(int lastevolum) {
		this.lastevolum = lastevolum;
	}
	
	// Overstyrer (override) superklassens toString()
	public String toString() {
		return super.toString() + ", lastevolum: " + lastevolum;
	}
	
	

}
