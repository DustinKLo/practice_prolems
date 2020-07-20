#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

// the user has to guess a nnumber from 0-5.
// output whether or not the person is correct

// need seed from clock

int main()
{
  srand(time(NULL));
  int ans = rand() % 6;
  int num;

  printf("guess a number between 0-5: ");
  scanf("%i", &num);

  if (num == ans)
  {
    printf("congratulations you guessed correctly!!\n");
  }
  else
  {
    printf("you guessed wrong the nunmber is %i\n", ans);
  }

  return 0;
}
