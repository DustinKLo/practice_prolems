import java.io.*;
import java.util.*;
import java.lang.Math;

public class GenerateParanthesis {
    int count;

    public GenerateParanthesis() {
        count = 1;
    }

    public void traverse(String pattern, int target, int numLeft, int numRight) {
        if (numLeft + numRight > target) {
            return;
        }
        if (numLeft < numRight) {
            return;
        }
        if (numLeft + numRight == target) {
            if (numLeft == numRight) {
                System.out.printf("%d: %s\n", this.count, pattern);
                this.count++;
            }
        }
        this.traverse(pattern.concat("("), target, numLeft + 1, numRight);
        this.traverse(pattern.concat(")"), target, numLeft, numRight + 1);
    }

    public void generateParanthesis(int num) {
        if (num % 2 != 0) {
            System.out.println("Odd number of paranthesis!!!");
            return;
        }
        this.count = 1;
        System.out.printf("Number of parenthesis: %d \n", num);
        this.traverse("", num, 0, 0);
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
