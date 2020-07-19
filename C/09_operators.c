#include <stdio.h>

int main()
{
  int x = 10;
  printf("x: %d\n", x);

  x++;
  printf("x: %d\n", x);

  int y = 2 + 3 * 4 / (3 - 2);
  printf("y: %i\n", y);

  int z = 5 % 2; // 1

  return 0;
}
