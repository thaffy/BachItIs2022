import java.util.ArrayList;

public class DiktKontroll {
	
	// Ordliste for enkel versjon av dikt
	private ArrayList<String> ordliste = new ArrayList<String>();
	
	// Ordlister for avansert versjon av dikt
	private ArrayList<String> artikkelListe = new ArrayList<String>();
	private ArrayList<String> adjektivListe = new ArrayList<String>();
	private ArrayList<String> substantivListe = new ArrayList<String>();
	private ArrayList<String> verbListe = new ArrayList<String>();
	
	// Enkel dikt
	public ArrayList<String> registrerOrd(String inputOrd) {
		ordliste.add(inputOrd);
		return ordliste;	
	}
	
	public String genererDikt() {
		
		if (ordliste.isEmpty()) {
			// Hvis ingen ord er registrert vil programmet ikke kunne finne lengden på lista, og kræsjer.
			return "Ingen ord er registrert i systemet." + "\n" + "Registrer noen ord og prøv på nytt!";
		}
		else {
			// Programmet genererer diktet først når 1 eller flere ord er lagt til
			int listeLengde = ordliste.size();
			String dikt = "";
			
			// Løkke i løkke for å legge til 4 ord på 4 linjer.
			for(int i = 1; i < 5; i++) {
				for(int j = 1; j < 5; j++) {
					int tilfeldigTall = (int)(Math.random() * (listeLengde));
					dikt += ordliste.get(tilfeldigTall) + " ";
				}
				dikt += "\n";
			}
			return dikt;
		}
	}
	// Slutt enkelt dikt
	
	
	// Avansert Dikt
	public ArrayList<String> regArtikkel(String inputArtikkel) {
		artikkelListe.add(inputArtikkel);
		return artikkelListe;	
	}
	public ArrayList<String> regAdjektiv(String inputAdjektiv) {
		adjektivListe.add(inputAdjektiv);
		return adjektivListe;	
	}
	public ArrayList<String> regSubstantiv(String inputSubstantiv) {
		substantivListe.add(inputSubstantiv);
		return substantivListe;	
	}
	public ArrayList<String> regVerb(String inputVerb) {
		verbListe.add(inputVerb);
		return verbListe;	
	}
	
	public String genererAvansertDikt() {
		boolean feilMelding = avansertTomListe();
		if (feilMelding) {
			// Hvis ingen ord er registrert vil programmet ikke kunne finne lengden på lista, og kræsjer.
			return "Ingen ord er registrert i systemet." + "\n" + "Registrer noen ord i hver kategori og prøv på nytt!";
		}
		else {
			String avansertDikt = "";
			
			int artikkelLengde = artikkelListe.size();
			int adjektivLengde = adjektivListe.size();
			int substantivLengde = substantivListe.size();
			int verbLengde = verbListe.size();
			
			for(int k = 1; k < 5; k++) {
	
				int tilfeldigArtikkel = (int)(Math.random() * (artikkelLengde));
				int tilfeldigAdjektiv = (int)(Math.random() * (adjektivLengde));
				int tilfeldigSubstantiv = (int)(Math.random() * (substantivLengde));
				int tilfeldigVerb = (int)(Math.random() * (verbLengde));
				
				avansertDikt += artikkelListe.get(tilfeldigArtikkel) + " ";
				avansertDikt += adjektivListe.get(tilfeldigAdjektiv) + " ";
				avansertDikt += substantivListe.get(tilfeldigSubstantiv) + " ";
				avansertDikt += verbListe.get(tilfeldigVerb);
			
				avansertDikt += "\n";
			}
			return avansertDikt;
		}
	}
	
	public boolean avansertTomListe() {
		boolean tomListeEksisterer = false;
		if (artikkelListe.isEmpty()) tomListeEksisterer = true;
		if (adjektivListe.isEmpty()) tomListeEksisterer = true;
		if (substantivListe.isEmpty()) tomListeEksisterer = true;
		if (verbListe.isEmpty()) tomListeEksisterer = true;
		
		return tomListeEksisterer;
	}
}
