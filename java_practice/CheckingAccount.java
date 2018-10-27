import java.io.*;

public class CheckingAccount {
   private double balance;
   private int number;
   
   public CheckingAccount(int number) {
      this.number = number;
   }
   
   public void deposit(double amount) {
      balance += amount;
   }
   
   public void withdraw(double amount) {
      if(amount <= balance) {
         balance -= amount;
      } else {
         double needs = amount - balance;
         // throw new InsufficientFundsException(needs);
      }
   }
   
   public double getBalance() {
      return balance;
   }
   
   public int getNumber() {
      return number;
   }

   public static void main(String args[]) {
      CheckingAccount checking1 = new CheckingAccount(1337);
      checking1.deposit(10000);
      System.out.println("checking1's balance is: " + checking1.getBalance());
      checking1.withdraw(100);
      System.out.println("checking1's balance is: " + checking1.getBalance());

      CheckingAccount checking2 = new CheckingAccount(337);
      checking2.deposit(10000);
      System.out.println("checking2's balance is: " + checking2.getBalance());
      checking2.withdraw(100);
      System.out.println("checking2's balance is: " + checking2.getBalance());
      checking2.deposit(100);
      System.out.println("checking2's balance is: " + checking2.getBalance());
   }
}