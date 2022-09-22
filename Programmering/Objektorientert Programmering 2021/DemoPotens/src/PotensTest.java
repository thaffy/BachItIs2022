public class PotensTest {
    public static void main(String[] args) {
        int grunntall = 2;
        int eksponent = 20;
        System.out.println(grunntall + " opphøyd i " + eksponent + " blir " + potens(grunntall,eksponent));
    }


    public static int potens(int grunntall, int eksponent) {
        if (eksponent ==1) return grunntall;
        else return potens(grunntall,eksponent - 1)*grunntall;
    }
}
