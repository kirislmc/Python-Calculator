import java.util.Scanner;

public class RectangleCalculator {

    public static void main(String[] args) {

            Scanner scanner = new Scanner(System.in);

            System.out.println("Enter the Wide(in cm): ");
            double wide = scanner.nextDouble();

            System.out.println("Enter the height(in cm): ");
            double height = scanner.nextDouble();

            double sum = wide * height;

            System.out.println("The area of you rectangle is " + sum + "cm²" );

            scanner.close();

    }
}