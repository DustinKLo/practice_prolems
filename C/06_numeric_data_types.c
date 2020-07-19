#include <stdio.h>

int main()
{
  int dogs = 6;

  // use double if number is very specific, ie 456.3455435375897
  // doubles are more standard

  // floats take up less space

  printf("%i %f %f\n", 1, 1111.11111111, 1.1111F);

  // scientific notation, ie 25000
  float scino = 2.5e4;
  printf("%f\n", scino);

  /*
  conversion characters
  -------------------------

  %f - decimal notation
  %e - scientific notation
  %g - computer decides
  */

  double testdbl = 2.5e7;
  printf("%f\n", testdbl);
  printf("%e\n", testdbl);
  printf("%g\n", testdbl);

  double testdbl2;
  printf("\nenter number: \n");
  scanf("%lf", &testdbl2);
  printf("%f\n", testdbl2);
  printf("%e\n", testdbl2);
  printf("%g\n", testdbl2);

  return 0;
}
