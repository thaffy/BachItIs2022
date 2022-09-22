
public class Buss extends Kjøretøy {
	
	private int antallplasser;

	public Buss(String regnr, String fabrikat, int antallplasser) {
		super(regnr, fabrikat);
		this.antallplasser = antallplasser;
	}

	public int getAntallplasser() {
		return antallplasser;
	}

	public void setAntallplasser(int antallplasser) {
		this.antallplasser = antallplasser;
	}
	
	// Overstyrer (override) superklassens toString()
	public String toString() {
		return super.toString() + ", antall plasser: " + antallplasser;
	}
	
	
	
}
