
public class TegneKontroll {
	
	public String tegnTrekant(int antallLinjer) {
		// Lager en tom String
		String tegning = "";
		int antallStjerner = 1;
		// Løkke for å lage trekantens linjer:
		for(int i = 0; i < antallLinjer;i++) {
			antallStjerner++;
			// Indre løkke som skriver stjerner på en linje:
			for(int j = 1; j < antallStjerner; j++) {
				tegning +='*';
			} // Slutt indre løkke
			
			// Legger til linjeskift:
			tegning += "\n";
			
		} // Slutt ytre løkke
		//Returnerer tegning:
		return tegning;
	}
	
	public String tegnPyramide(int antall) {
		String tegning = "";
		// Problemet her er å finne ut hvor programmet skal begynne å tegne..
		// Ytre løkke:
		for(int i = 1; i < antall * 2; i+=2) {
			// Indre løkke som skriver ut mellomrom til der stjernene skal starte:
			for(int j = 0; j < (antall - i / 2); j++)
				tegning += " ";
			
			// Ny løkke skriver ut stjerner:
			for(int k = 0; k < i; k++) {
				tegning +='*';
			}
			
			// Legger til linjeskift
			tegning += "\n";
		}

				
				
		return tegning;
	}

}
