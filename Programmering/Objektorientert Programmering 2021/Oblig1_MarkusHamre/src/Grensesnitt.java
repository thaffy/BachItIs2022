import javax.swing.JOptionPane;

public class Grensesnitt {
	
	DiktKontroll kontroll = new DiktKontroll();
	
	// Hovedmeny
	private final String[] ALTERNATIVER = {"Enkelt Dikt","Avansert Dikt","Avslutt"};
	
	// Submenyer for enkelt dikt, avansert dikt og ordregistrering i avansert dikt.
	private final String[] ENKELTDIKT = {"Registrer Ord","Generer Enkelt Dikt","Tilbake"};
	private final String[] AVANSERTDIKT = {"Registrer Ord", "Generer Avansert Dikt","Tilbake"};
	private final String[] ORDREGISTRERING = {"Artikkel","Adjektiv","Substantiv","Verb","Tilbake"};
	
	// Hovedmeny
	public int lesValg() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Diktprogram",JOptionPane.DEFAULT_OPTION,JOptionPane.PLAIN_MESSAGE,null,ALTERNATIVER,ALTERNATIVER[0]);
		return valg;
	}
	
	// Enkelt dikt
	public int lesValgEnkel() {
		int valgEnkel = JOptionPane.showOptionDialog(null, "Gjør et valg", "Enkelt Dikt", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ENKELTDIKT, ENKELTDIKT[0]);
		return valgEnkel;
	}
	
	// Avansert Dikt
	public int lesValgAvansert() {
		int valgAvansert = JOptionPane.showOptionDialog(null, "Gjør et valg", "Avansert Dikt", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, AVANSERTDIKT, AVANSERTDIKT[0]);
		return valgAvansert;
	}
	
	// Ordregistrering innenfor submenyen Avansert Dikt
	public int lesValgRegistrer() {
		int valgRegistrer = JOptionPane.showOptionDialog(null, "Gjør et valg", "Ordregistrering", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ORDREGISTRERING, ORDREGISTRERING[0]);
		return valgRegistrer;
	}
	
	public void hovedmeny() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValg();
			switch(valg) {
			case 0 : enkeltDiktMeny();
				break;
			case 1 : avansertDiktMeny();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void enkeltDiktMeny() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValgEnkel();
			switch(valg) {
			case 0 : registrerOrd();
				break;
			case 1 : genererDikt();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void avansertDiktMeny() {
		boolean fortsett = true;
		while(fortsett) {
			int valgAvansert = lesValgAvansert();
			switch(valgAvansert) {
			case 0 : registrerOrdAvansert();
				break;
			case 1 : genererAvansertDikt();
				break;
			default : fortsett = false;
			}
		}
	}
	
	public void registrerOrdAvansert() {
		boolean fortsett = true;
		while(fortsett) {
			int valgRegistrer = lesValgRegistrer();
			switch(valgRegistrer) {
			case 0 : regArtikkel();
				break;
			case 1 : regAdjektiv();
				break;
			case 2 : regSubstantiv();
				break;
			case 3 : regVerb();
				break;
			default : fortsett = false;
			}
		}
		
	}
	

	
	public void registrerOrd() {
		while(true) {
			String inputOrd = JOptionPane.showInputDialog("Legg til et ord i lista: ");
			if (inputOrd == null) break;
			if (!inputOrd.isEmpty()) kontroll.registrerOrd(inputOrd);
		}	
	}
	
	public void genererDikt() {
		String dikt = kontroll.genererDikt();
		JOptionPane.showMessageDialog(null,dikt);	
	}
	// Slutt enkelt dikt
	
	// Avansert Dikt
	// Bruker while-løkker for at bruker skal kunne skrive inn så mange ord de ønsker. Løkka avsluttes når
	// bruker trykker cancel eller lukker vinduet ved bruk av break.
	// isEmpty sjekker at ordene som sendes til DiktKontroll har innhold, da dette kan påvirke diktresultatet ved utskrift.
	public void regArtikkel() {
		while(true) {
			String inputArtikkel = JOptionPane.showInputDialog("Legg til en artikklel: ");
			if (inputArtikkel == null) break;
			if (!inputArtikkel.isEmpty()) kontroll.regArtikkel(inputArtikkel);
			
		}
	}
	public void regAdjektiv() {
		while(true) {
			String inputAdjektiv = JOptionPane.showInputDialog("Legg til et adjektiv: ");
			if (inputAdjektiv == null) break;
			if (!inputAdjektiv.isEmpty()) kontroll.regAdjektiv(inputAdjektiv);
		}
	}
	public void regSubstantiv() {
		while(true) {
			String inputSubstantiv = JOptionPane.showInputDialog("Legg til et substantiv: ");
			if (inputSubstantiv == null) break;
			if (!inputSubstantiv.isEmpty()) kontroll.regSubstantiv(inputSubstantiv);
		}
	}
	public void regVerb() {
		while(true) {
			String inputVerb = JOptionPane.showInputDialog("Legg til et verb: ");
			if (inputVerb == null) break;
			if (!inputVerb.isEmpty()) kontroll.regVerb(inputVerb);
		}
	}
	public void genererAvansertDikt() {
		String avansertDikt = kontroll.genererAvansertDikt();
		JOptionPane.showMessageDialog(null, avansertDikt);	
	}
}
