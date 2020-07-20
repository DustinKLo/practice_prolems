#include <stdio.h>
#include <math.h>

int main()
{
  double x, y;

  printf("Enter x: ");
  scanf("%lf", &x);

  printf("Enter y: ");
  scanf("%lf", &y);

  double z = sqrt(x * x + y * y);
  printf("side z: %g\n", z);

  return 0;
}
