#include <stdio.h>

int main()
{
  int eggs;
  printf("enter number of eggs: ");
  scanf("%i", &eggs);

  double dz = (double)eggs / 12;
  printf("you have %f dozen eggs \n", dz);

  return 0;
}
