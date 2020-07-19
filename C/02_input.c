#include <stdio.h>

int main()
{
  int r;
  double area;
  
  printf("enter radius: ");
  scanf("%d", &r);
  printf("You entered %d.\n", r);

  area = 3.14159 * r * r;
  printf("the area is circle is %f\n", area);

  return 0;
}
