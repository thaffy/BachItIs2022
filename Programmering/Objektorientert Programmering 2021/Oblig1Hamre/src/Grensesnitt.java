import javax.swing.JOptionPane;

public class Grensesnitt {
	// Menyvalg
	private final String[] ALTERNATIVER = {"Registrer Ord", "Lag Dikt", "Avslutt"};
	
	DiktKontroll diktKontroll = new DiktKontroll();
	public int lesValg() {
		int valg = JOptionPane.showOptionDialog(null, "Gjør et valg", "Diktprogram", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ALTERNATIVER, ALTERNATIVER[0]);
		return valg;
	
	}
	public void meny() {
		// Bruker en løkke styrt av en boolsk:
		boolean fortsett = true;
		while(fortsett) {
			// Skriver ut meny og leser menyvalg:
			int valg = lesValg();
			// Bruker en case for å behandle valg
			switch(valg) {
			case 0 : registrerOrd();
				break;
			case 1 : genererDikt();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void registrerOrd() {
		String inputOrd = JOptionPane.showInputDialog("Legg til et ord i ordlista: ");
		String ordliste = diktKontroll.registrerOrd(inputOrd);
	}
	
	public void genererDikt() {
		String Dikt = diktKontroll.genererDikt(Dikt);
		JOptionPane.showMessageDialog(null, generertDikt);
		
	}

}
