import java.util.Scanner;

public class Hilsen {

	public static void main(String[] args) {
		Scanner kbd = new Scanner(System.in);
		System.out.println("Hva heter du?");
		String navn = kbd.next();
		System.out.println("Hallo, " + navn);

	}

}
