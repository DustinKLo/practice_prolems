#include <stdio.h>
#include <stdbool.h>

int main()
{
  char ynPizza;

  printf("do you love pizza? (y/n) ");
  scanf("%c", &ynPizza);

  bool isPizzaHealthy = (ynPizza == 'y') ? true : false;

  if (isPizzaHealthy)
  {
    printf("welcome to my pizza app!\n");
  }
  else
  {
    printf("GTFO of mu pizza shop!\n");
  }

  return 0;
}
