import java.io.*;


public class CopyFile {
   public static void main(String args[]) throws IOException {
      FileInputStream in = null;
      FileOutputStream out = null;

      try {
         in = new FileInputStream("input.txt");
         out = new FileOutputStream("output.txt");
         
         int c;
         while ((c = in.read()) != -1) {
            System.out.println(c);
            out.write(c);
         }
         System.out.println('\n');

      } finally {
         if (in != null) {
            System.out.println(in);
            in.close();
         }
         if (out != null) {
            System.out.println(out);
            out.close();
         }
      }
   }
}