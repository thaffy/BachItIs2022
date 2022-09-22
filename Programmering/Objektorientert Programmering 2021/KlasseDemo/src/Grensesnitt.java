import javax.swing.JOptionPane;

public class Grensesnitt {
	Kontroll kontroll = new Kontroll();
	final String[] ALTERNATIVER = {"Ny ansatt", "Ny student","Søk","Avslutt"};
	
	public void meny() {
		boolean fortsett = true;
		while(fortsett) {
			@SuppressWarnings("unused")
			int valg = JOptionPane.showOptionDialog(
					null, 
					"Gjør et valg:", 
					"Arbeidstagermeny", 
					JOptionPane.DEFAULT_OPTION, 
					JOptionPane.PLAIN_MESSAGE, 
					null,
					ALTERNATIVER,
					ALTERNATIVER[0]);
		}
	}
	

}
