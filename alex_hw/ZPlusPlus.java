import java.util.Stack;
import java.util.HashMap;

public class ZPlusPlus {
	public static Boolean validate(String inputString) {
		Stack<Character> stack = new Stack<>();

		HashMap<Character, Character> mapper = new HashMap<>();
		mapper.put(')', '(');
		mapper.put(']', '[');
		mapper.put('}', '{');

		for (int i = 0; i < inputString.length(); i++) {
			char c = inputString.charAt(i);
			if (c == '(' || c == '[' || c == '{') {
				stack.push(c);
				continue;
			} else if (stack.isEmpty() || mapper.get(c) != stack.peek()) {
				return false;
			}
			stack.pop();
		}
		return (stack.size() == 0) ? true : false;
	}

	public static void main(String[] args) {
		String x = "[]{}()";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "{([])}";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "()[{}]";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "[{}()]";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "[({)}]";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "()()()()()()((()))()()(((())))(())";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "()()()()()()((()))()()(((())))(())(";
		System.out.printf("%s: %b\n", x, validate(x));

		x = "()()()()()()((()))()()(((())))(()))";
		System.out.printf("%s: %b\n", x, validate(x));
	}
}
