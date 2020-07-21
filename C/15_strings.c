#include <stdio.h>
#include <string.h>

int main()
{
  printf("what is your favorite food? ");

  char f[50];

  // subtract one from string length for safety
  scanf("%49s", f);
  printf("your fave food is %s\n", f);
  printf("%s is length %ld\n", f, strlen(f));

  return 0;
}
