package Assosiasjoner;

public class Testklient {

    public static void main(String[] args) {
        Kontroll kontroll = new Kontroll();

        kontroll.nyPostadresse("3500","Hønefoss");
        kontroll.nyPostadresse("3000","Drammen");

        kontroll.nyPerson("Ole","Veien 3","3500");
        kontroll.nyPerson("Lise","Lierveien 2","3000");

        // For å registrere et kjøretøy må vi ha et person-objekt
        Person person = kontroll.finnPerson("Ole");

        // Legger til et nytt kjøretøy:
        Kjoretoy kjoretoy = new Kjoretoy("AB12345","Subaru",person);

        // Legger kjøretøyet inn i kontroll:
        // registrerer kjøretøyet på personen:
        kontroll.nyttKjoretoy(kjoretoy);
        person.nyttKjoretoy(kjoretoy);

        System.out.println(kjoretoy);
    }

}
