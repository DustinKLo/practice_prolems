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

  int i = 25;
  while (i > 0)
  {
    printf("i: %i\n", i);
    i--;
  }

  int i2 = 100;
  i2 += 100;
  i2 -= 100;
  i2 *= 2;
  i2 /= 5;
  i2 %= 5;

  int d1, d2;
  d1 = (d2 = 5);

  return 0;
}
