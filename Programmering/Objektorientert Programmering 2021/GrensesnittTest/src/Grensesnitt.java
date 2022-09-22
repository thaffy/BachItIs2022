import javax.swing.JOptionPane;

public class Grensesnitt {
	
	//DiktKontroll kontroll = new DiktKontroll();
	private final String[] ALTERNATIVER = {"Enkelt Dikt","Avansert Dikt","Avslutt"};
	
	private final String[] HOVEDMENY = {"Enkelt Dikt","Avansert Dikt","Tilbake"};
	private final String[] ENKELTDIKT = {"Registrer Ord","Generer Enkelt Dikt","Tilbake"};
	private final String[] AVANSERTDIKT = {"Registrer Ord, Generer Avansert Dikt","Tilbake"};
	//private final String[] ORDREGISTRERING = {"Artikkel","Adjektiv","Substantiv","Verb","Tilbake"};
	
	//public int lesValg() {
		//int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
		//return valg;
	//}
	
	public void meny() {
		
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,HOVEDMENY,HOVEDMENY[0]);
		
		boolean fortsett = true;
		while(fortsett) {
			switch(valg) {
			case 0 : enkelmeny();
				break;
			case 1 : avansertmeny();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void enkelmeny() {
		
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,ENKELTDIKT,ENKELTDIKT[0]);
		boolean fortsett = true;
		while(fortsett) {
			switch (valg) {
			case 0 : registrerOrd();
				break;
			case 1 : genererDikt();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void avansertmeny() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,AVANSERTDIKT,AVANSERTDIKT[0]);
		
		boolean fortsett = true;
		while(fortsett) {
			switch (valg) {
			case 0 : registrerOrd();
				break;
			case 1 : genererDikt();
				break;
			default : fortsett = false;
			}
		}
	}
	
	
	
	public void registrerOrd() {
		for(int i = 1; i < 5; i++) {
			String inputOrd = JOptionPane.showInputDialog("Legg til 4 ord i ordlista: ");
			//kontroll.registrerOrd(inputOrd);
		}

		
	}
	
	public void genererDikt() {
		//String dikt = kontroll.genererDikt();
		//JOptionPane.showMessageDialog(null,dikt);

		
	}

}
