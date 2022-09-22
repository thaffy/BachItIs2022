import javax.swing.JOptionPane;

public class Grensesnitt {
	// Menyvalgene:
	private final String[] ALTERNATIVER = {"Trekant", "Pyramide", "Avslutt"};
	// Lager et objekt av TegneKontroll:
	TegneKontroll tegneKontroll = new TegneKontroll();
	
	// Metode som skriver ut hovedmenyen og returnerer valget:
	public int lesValg() {
		// Bruker showOptionDialog:
		int valg = JOptionPane.showOptionDialog(null, "Gjør et valg", "Tegneprogram", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ALTERNATIVER, ALTERNATIVER[0]);
		return valg;
	}
	
	// Metoden meny() behandler hovedmenyen og valgene:
	public void meny() {
		// Bruker en løkke styrt av en boolsk:
		boolean fortsett = true;
		while(fortsett) {
			// Skriver ut meny og leser menyvalg:
			int valg = lesValg();
			// Bruker en case for å behandle valg
			switch(valg) {
			case 0 : tegnTrekant();
				break;
			case 1 : tegnPyramide();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void tegnTrekant() {
		int antall = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer:"));
		// Kaller metoden tegnTrekant() i tegneKontroll
		String tegning = tegneKontroll.tegnTrekant(antall);
		// Viser figuren
		JOptionPane.showMessageDialog(null, tegning);
	}
	
	public void tegnPyramide() {
		int antall = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer:"));
		// Kaller metoden tegnPyramide() i tegneKontroll
		String tegning = tegneKontroll.tegnPyramide(antall);
		// Viser figuren
		JOptionPane.showMessageDialog(null, tegning);
		
	}

}
