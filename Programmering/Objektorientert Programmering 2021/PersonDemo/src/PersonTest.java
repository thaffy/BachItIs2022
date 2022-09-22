
public class PersonTest {

	public static void main(String[] args) {
		Person p1 = new Person("Lise", 23);
		Person p2 = new Person("Ole", 22);
		System.out.println(p1.toString());
		System.out.println(p2.getNavn());
		p2.setNavn("Hans");
		System.out.println(p2.getNavn());
		System.out.println(p2.toString());
	}

}
