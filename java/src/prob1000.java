import java.util.Scanner;

public class prob1000 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        aaa(a, b);
        minus(a, b);
    }

    private static void minus(int a, int b) {
        System.out.println(a + b);
    }

    private static void aaa(int a, int b) {
        minus(a, b);
    }

}
