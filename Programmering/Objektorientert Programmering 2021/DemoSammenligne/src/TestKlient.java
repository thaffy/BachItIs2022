
public class TestKlient {

	public static void main(String[] args) {
		Poststed p1 = new Poststed(3502,"Hønefoss");
		Poststed p2 = new Poststed(3511,"Hønefoss");
		Poststed p3 = new Poststed(3502,"Hønefoss");
		Poststed p4 = new Poststed(6929,"Molde");
		Poststed p5 = new Poststed(3000,"Drammen");
		
		Student s1 = new Student(1234,"Ole",p1);
		Student s2 = new Student(5678,"Ole",p2);

		
		// Tester på likhet:
		if(p1.equals(p2)) System.out.println("p1 og p2 er samme poststed!");
		else System.out.println("p1 og p2 er ikke samme poststed :(");
		if(p1.equals(p3)) System.out.println("p1 og p3 er samme poststed!");
		else System.out.println("p1 og p3 er ikke samme poststed :(");
		
		if(s1.equals(s2)) System.out.println("s1 og s2 er samme navn");
		else System.out.println("s1 og s2 har ikke samme navn :(");
		
	}

}
