import java.io.*;
import java.util.*;
import java.lang.Math;

public class GenerateParanthesis {
    ArrayList<String> patterns;

    public GenerateParanthesis() {
        patterns = new ArrayList<String>();
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
                this.patterns.add(pattern);
            }
        }
        this.traverse(pattern.concat("("), current + 1, target, numLeft + 1, numRight);
        this.traverse(pattern.concat(")"), current + 1, target, numLeft, numRight + 1);
    }

    public void generateParanthesis(int num) {
        if (num % 2 != 0) {
            System.out.println("Odd number of paranthesis!!!");
        }
        this.patterns.clear();
        System.out.printf("Number of parenthesis: %d \n", num);
        this.traverse("", 0, num, 0, 0);

        for (int i = 0; i < this.patterns.size(); i++) {
            System.out.printf("%d: %s\n", i + 1, this.patterns.get(i));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        GenerateParanthesis testCase = new GenerateParanthesis();
        testCase.generateParanthesis(2);
        testCase.generateParanthesis(4);
        testCase.generateParanthesis(6);
        testCase.generateParanthesis(8);
        testCase.generateParanthesis(10);
        testCase.generateParanthesis(12);
    }
}
