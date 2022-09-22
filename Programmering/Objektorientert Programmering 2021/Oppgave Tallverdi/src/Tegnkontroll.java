
public class Tegnkontroll {
	
	public String lagVerdier(char start, char slutt) {
		// Oppretter en tom string:
		String utTekst = "";
		// Lager en integer ut fra char'ene:
		int først = start; // Fordi en char-verdi egentlig er et heltall (int)
		int sist = slutt;
		// verdi skal brukes inne i løkka
		int verdi = start;
		for(int i = først; i < sist + 1;i++) {
			// Bygger opp utteksten
			utTekst += "Tegnet " + start + " har verdien " + verdi + "\n";
			verdi++;
			start = (char)verdi;
		}
		// Returnerer den ferdige teksten
		return utTekst;
	}

}
