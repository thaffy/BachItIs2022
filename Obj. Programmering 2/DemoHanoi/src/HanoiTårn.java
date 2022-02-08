import javax.swing.*;

public class HanoiTårn {
    public static void main(String[] args) {
        int n = Integer.parseInt(JOptionPane.showInputDialog("Skriv antall skiver: "));
        System.out.println("Flytting er:");
        flytt(n,'A','B','C');
    }

    // Reskursiv metode der n er antall skiver
    public static void flytt(int n, char fraTårn, char tilTårn, char ekstraTårn) {
        if(n == 1) System.out.println("Flytt skive " + n + " fra " + fraTårn + " til " + tilTårn);
        else {
            flytt(n - 1,fraTårn,ekstraTårn,tilTårn);
            System.out.println("Flytt skive " + n + " fra " + fraTårn + " til " + tilTårn);
            flytt(n - 1, ekstraTårn, tilTårn, fraTårn);
        }
    }
}
