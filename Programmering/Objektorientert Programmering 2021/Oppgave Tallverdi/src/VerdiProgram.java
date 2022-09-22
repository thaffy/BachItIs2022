import javax.swing.JOptionPane;

public class VerdiProgram {

	public static void main(String[] args) {
		// Lager et objekt av klassen Tegnkontroll
		Tegnkontroll kontroll = new Tegnkontroll();
		// Leser valg som en string
		String lestStart = JOptionPane.showInputDialog("Skriv første tegn:");
		// Henter ut tegnet:
		char start = lestStart.charAt(0);
		// Leser slutt:
		String lestSlutt = JOptionPane.showInputDialog("Skriv siste tegn:");
		char slutt = lestSlutt.charAt(0);
		// Kaller lagVerdier
		String utTekst = kontroll.lagVerdier(start, slutt);
		JOptionPane.showMessageDialog(null, utTekst);
		

	}

}
