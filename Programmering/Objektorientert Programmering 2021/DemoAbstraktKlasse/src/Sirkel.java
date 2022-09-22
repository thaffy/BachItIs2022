
public class Sirkel extends Figur {
	private double radius;
	
	public Sirkel(double radius) {
		super();
		this.radius = radius;
	}

	@Override
	public double beregnAreal() {
		return Math.PI*radius*radius;
	}

}
