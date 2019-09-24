import java.io.*;
import java.util.*;
import java.lang.Math;

public class GenerateParanthesis {
    int count;

    public GenerateParanthesis() {
        count = 1;
    }

    public void traverse(String pattern, int current, int target, int numLeft, int numRight) {
        if (current > target) {
            return;
        }
        if (numLeft < numRight) {
            return;
        }
        if (current == target) {
            if (numLeft == numRight) {
                System.out.printf("%d: %s\n", this.count, pattern);
                this.count++;
            }
        }
        this.traverse(pattern.concat("("), current + 1, target, numLeft + 1, numRight);
        this.traverse(pattern.concat(")"), current + 1, target, numLeft, numRight + 1);
    }

    public void generateParanthesis(int num) {
        if (num % 2 != 0) {
            System.out.println("Odd number of paranthesis!!!");
            return;
        }
        this.count = 1;
        System.out.printf("Number of parenthesis: %d \n", num);
        this.traverse("", 0, num, 0, 0);
        System.out.println();
    }

    public static void main(String[] args) {
        GenerateParanthesis testCase = new GenerateParanthesis();
        testCase.generateParanthesis(2);
        testCase.generateParanthesis(4);
        testCase.generateParanthesis(6);
        testCase.generateParanthesis(8);
        testCase.generateParanthesis(10);
    }
}
