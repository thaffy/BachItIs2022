import javax.swing.JOptionPane;

public class Ganger {

	public static void main(String[] args) {
		// Spør etter en startverdi:
		String lestStart = JOptionPane.showInputDialog("Skriv startverdi:");
		int start = Integer.parseInt(lestStart);
		// Leser sluttverdi i én setning:
		int slutt = Integer.parseInt(JOptionPane.showInputDialog("Skriv sluttverdi:"));
		// Ytre Løkke som skriver ut overskrift for del av gangetabllen:
		for(int i = start; i < slutt+1; i++) {
			System.out.println();
			System.out.println(i + "-gangen:");
			// Indre løkke som regner ut ganging fra 1 til 10
			for(int j = 1; j < 11; j++) {
				//i-telleren fra ytre løkke ganges med j-telleren fra indreløkke
				System.out.println(i + " x " + j + " = " + i*j);
			}
		}
	}

}
