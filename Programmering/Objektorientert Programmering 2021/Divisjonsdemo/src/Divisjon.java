import java.util.Formatter;
import javax.swing.JOptionPane;
public class Divisjon {

	public static void main(String[] args) {
		String lestTall = JOptionPane.showInputDialog("Skriv et tall: ");
		int tall1 = Integer.parseInt(lestTall);
		lestTall = JOptionPane.showInputDialog("Skriv et tall til: ");
		int tall2 = Integer.parseInt(lestTall);
		// Foretar en heltallsdivisjon:
		int svar = tall1/tall2;
		// Presenterer svaret:
		JOptionPane.showMessageDialog(null, "Svaret på heltallsdivisjon er " + svar);
		// "Vanlig" divisjon:
		double svar2 = (double)tall1/tall2;
		JOptionPane.showMessageDialog(null, "Svaret på vanlig divisjon er " + svar2);
		// Modulus (rest)
		int svar3 = tall1%tall2;
		JOptionPane.showMessageDialog(null, "Resultatet av modulus:" + svar3);
		// Formattert utskrift i konsoll
		System.out.printf("%.2f", svar2);
		// For formattert utskrift i meldingsboks
		Formatter formatør = new Formatter();
		formatør.format("%.2f", svar2);
		JOptionPane.showMessageDialog(null, "Formattert desimaltall: " + formatør.toString());
		
	}

}
