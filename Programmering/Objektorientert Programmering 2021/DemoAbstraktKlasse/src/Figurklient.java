
public class Figurklient {

	public static void main(String[] args) {
		Sirkel sirkel = new Sirkel(10);
		Trekant trekant = new Trekant(5,6);
		Kvadrat kvadrat = new Kvadrat(4);
		
		System.out.println("Arealet til sirkelen: " + sirkel.beregnAreal());
		System.out.println("Arealet til trekanten: " + trekant.beregnAreal());
		System.out.println("Arealet til kvadratet: " + kvadrat.beregnAreal());

	}

}
