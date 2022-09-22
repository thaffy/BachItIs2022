package lambdademo;

public class TesteLambda {
    public static void main(String[] args) {
        // Lager kalkulatorerer:
        Kalkulator addisjon = (a, b) -> a + b;
        Kalkulator subtraksjon = (a, b) -> a - b;
        Kalkulator multiplikasjon = (a, b) -> a * b;
        Kalkulator divisjon = (a, b) -> a / b;

        // Bruker kalkulatorene
        System.out.println("Addisjon: " + addisjon.operasjon(7, 2));
        System.out.println("Subtraksjon: " + subtraksjon.operasjon(7, 2));
        System.out.println("Multiplikasjon: " + multiplikasjon.operasjon(7, 2));
        System.out.println("Divisjon: " + divisjon.operasjon(7, 2));
    }
}
