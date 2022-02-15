package bilregister;

import javax.swing.JOptionPane;
import java.util.ArrayList;

public class BilGrensesnitt {
	Bilregister bilkontroll = new Bilregister();
	private String[ ] ALTERNATIVER = {"Registrer eier","Registrer poststed","Registrer bil","Les fra fil","Skriv til fil","List ut eiere","Avslutt"};	
	private final int REG_EIER = 0;
	private final int REG_POST = 1;
	private final int REG_BIL = 2;
	private final int LES_FIL = 3;
	private final int SKRIV_FIL = 4;
	private final int EIERE = 5;
	private final int AVSLUTT = 6;	
	private String bilfil = "biler.txt";
	private String eierfil = "eiere.txt";
	private String postfil = "postnummere.txt";
	
	public void start() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValg();
			switch(valg) {
				case REG_EIER : regEier();
					break;
				case REG_POST : regPost();
					break;
				case REG_BIL : regBil();
					break;
				case LES_FIL : lesFiler();
					break;
				case SKRIV_FIL : skrivFiler();
					break;
				//case LES_POST: lesPostadresser();
				//	break;
				case EIERE: listEiere();
					break;
				case AVSLUTT : fortsett = false;
			} //switch
		} //while
	}
	
	public int lesValg( ) {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg","Bilregister",JOptionPane.DEFAULT_OPTION,
		JOptionPane.PLAIN_MESSAGE,null,ALTERNATIVER,ALTERNATIVER[0]);
		return valg;
	}
	
	public void listEiere() {
		ArrayList<Person> eiere = bilkontroll.hentEiere();
		String uttekst = "";
		for(int i = 0;i < eiere.size();i++) {
			Person person = eiere.get(i);
			uttekst += person.toString();
			uttekst += "\n";			
		}
		JOptionPane.showMessageDialog(null,  uttekst);
	}
	
	public void regEier() {
		String enavn = JOptionPane.showInputDialog("Etternavn:");
		String fnavn = JOptionPane.showInputDialog("Fornavn:");
		String pnr = JOptionPane.showInputDialog("Postnummer:");
		Postadresse padr = bilkontroll.postadresse(pnr);
		JOptionPane.showMessageDialog(null, padr.toString());
		bilkontroll.regEier(enavn, fnavn, padr);
	}
	
	public void lesFiler() {
		try {
			bilkontroll.lesAlleFiler();
		}catch(Exception e){JOptionPane.showMessageDialog(null,e.getMessage());}
	}
	
	public void skrivFiler() {
		try{
			bilkontroll.skrivAlleFiler();
		}catch(Exception e){JOptionPane.showMessageDialog(null,e.getMessage());}
	}
	
	public void regPost() {
		String pnr = JOptionPane.showInputDialog("Skriv postnummer: ");
		String pnavn = JOptionPane.showInputDialog("Skriv poststed: ");
		bilkontroll.regPost(pnr, pnavn);
	}
	
	public void lesPostadresser() {
		try {
			bilkontroll.lesPostadresser(postfil);
		}catch(Exception e){JOptionPane.showMessageDialog(null,e.getMessage());}
	}
	
	public void regBil() {
		String regnr = JOptionPane.showInputDialog("Skriv registreringsnummer: ");
		String merke = JOptionPane.showInputDialog("Skriv bilmerke: ");
		String modell = JOptionPane.showInputDialog("Skriv bilmodell: ");
		String enavn = JOptionPane.showInputDialog("Skriv eierens etternavn: ");
		Person eier = bilkontroll.finnEier(enavn);
		JOptionPane.showMessageDialog(null, eier.toString());
		bilkontroll.regBil(regnr, merke, modell,eier);
	}

}
