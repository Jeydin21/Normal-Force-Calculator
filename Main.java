import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Are you American? (y/n) ");
        boolean isAmerican = scanner.nextLine().equalsIgnoreCase("y");

        String weightQuestion = isAmerican ? "What is your weight in pounds?" : "What is your weight in kilograms?";
        System.out.println(weightQuestion);
        double weight = scanner.nextDouble();

        System.out.println(calculateNormalForce(weight, isAmerican));
    }

    public static String calculateNormalForce(double mass, boolean isAmerican) {
        double force;
        if (isAmerican) {
            force = (mass * 0.45359237) * 9.8; // Pounds to kilograms conversion
        } else {
            force = mass * 9.8;
        }
        return "Your normal force is " + String.format("%.3f", force) + " N";
    }
}