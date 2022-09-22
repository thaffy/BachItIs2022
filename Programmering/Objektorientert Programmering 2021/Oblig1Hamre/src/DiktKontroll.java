import java.util.ArrayList;

import javax.swing.JOptionPane;

public class DiktKontroll {
	
	
	public String placeholderOrdliste; {
		// Midlertidlig ordliste-array for test av generering.
		ArrayList<String> ordlisteTemp = new ArrayList<String>();
		ordlisteTemp.add("håper");
		ordlisteTemp.add("gulrot");
		ordlisteTemp.add("virrer");
		ordlisteTemp.add("grønn");
		ordlisteTemp.add("vinter");
		ordlisteTemp.add("snerrer");
		ordlisteTemp.add("borte");
		ordlisteTemp.add("lenge");
		ordlisteTemp.add("derfra");
		ordlisteTemp.add("sover");
		ordlisteTemp.add("løper");
		ordlisteTemp.add("sykkel");
		ordlisteTemp.add("rød");
		ordlisteTemp.add("blå");
		ordlisteTemp.add("gående");
		ordlisteTemp.add("sommer");
		ordlisteTemp.add("høst");
		
		
	}
	
	public String registrerOrd(String inputOrd) {
		String [] ordliste = new String[16];
		for(int i = 1; i < 17;i++) {
			ordliste[i] = inputOrd;
		}
			
		
		return (null);
		
		
		

		
	}
	
	public String genererDikt(String[] ordliste) {
		
		// Generer et tilfeldig tall mellom fra 0 til og med 16:
		int tilfeldigOrd = (int)(Math.random() * 17);
		
		String generertDikt = "";
		
		for(int i = 1; i < 17;i++) {
			for(int j = 1; j < 5;j++) {
				generertDikt += ordliste[tilfeldigOrd];
			}
			generertDikt += "\n";
		}
		
		
		
		return generertDikt;
		

		
		
	}


}
