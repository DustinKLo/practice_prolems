import java.util.*;

public class Person {
    int age;
    String name;
    String profession;

    Person(int age, String name, String profession) {
        this.age = age;
        this.name = name;
        this.profession = profession;
    }

    public static void printWhatever(String s) {
        System.out.println(s);
    }

    public static void doublePersonAge(Person p) {
        p.age = p.age * 2;
    }

    public static void swapFunction(int a, int b) {
      System.out.println("Before swapping(Inside), a = " + a + " b = " + b);
      // Swap n1 with n2
      int c = a;
      a = b;
      b = c;
      System.out.println("After swapping(Inside), a = " + a + " b = " + b);
   }

    public static void main(String[] args) {
        Person dustin = new Person(26, "Dustin", "data analyst");
        System.out.println("Dustin's age is " + dustin.age);
        System.out.println("Dustin's name is " + dustin.name);
        doublePersonAge(dustin);
        System.out.println("Dustin's age is " + dustin.age);
        doublePersonAge(dustin);
        System.out.println("Dustin's age is " + dustin.age);
        System.out.println("Dustin's profession is " + dustin.profession);

        printWhatever("I hate my job");

        int[] testArr = {1,2,3,4,5};
        for(int val: testArr) {
            System.out.println(val);
        }

        swapFunction(3, 4);
    }
}