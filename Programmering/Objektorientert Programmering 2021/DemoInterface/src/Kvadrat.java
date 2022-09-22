
public class Kvadrat implements Figur {
	private double side;
	
	public Kvadrat(double side) {
		super();
		this.side = side;
	}
	
	// Vi må implementere metoden beregnAreal():
	@Override
	public double beregnAreal() {
		return side*side;
	}

}
