public class Låntager {

    String kundenummer;
    String navn;
    String adresse;

    public Låntager(String kundenummer, String navn, String adresse) {
        this.kundenummer = kundenummer;
        this.navn = navn;
        this.adresse = adresse;
    }

    @Override
    public String toString() {
        return "Kundenummer: " + kundenummer + " - Navn: " + navn + " - Adresse: " + adresse;
    }
}
