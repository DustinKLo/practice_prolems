#include <stdio.h>
#include <stdbool.h> // makes booleans easier to work with

int main()
{
  // stdbool.h allows you to use bool keyword instead of _Bool
  // can use true or false instead of 1 and 0
  bool boolVar = true;

  printf("boolVar: %i %i\n", boolVar, boolVar + 10);

  return 0;
}
