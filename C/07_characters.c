#include <stdio.h>

int main()
{
  /*
  char - character
  character set - allowed characters
    - ASCII is also characters

  binary - "two states"

  %c is ASCII representation of integer
  */

  char x = 'a'; // integer value is 65
  printf("%c\n", x);

  char myChar;
  printf("enter character: ");
  scanf("%c", &myChar);
  printf("%c %i\n", myChar, myChar);

  int integer;
  printf("enter integer between 0 - 127: ");
  scanf("%d", &integer);
  printf("%c\n", integer);

  // match with ASCII
  char mathz = 'A' + '\t';
  printf("A(65) + \\t(11) = %c(%d)\n", mathz, mathz);

  return 0;
}
