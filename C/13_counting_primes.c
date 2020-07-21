#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool isPrime(int n)
{
  if (n == 2 || n == 3)
    return true;

  for (int i = 2; i < (int)sqrt(n) + 1; i++)
  {
    if (n % i == 0)
      return false;
  }
  return true;
}

int main()
{
  int n;
  printf("number to count to: ");
  scanf("%d", &n);

  if (n < 2)
  {
    printf("number must be greater than 1\n");
    return 1;
  }

  bool isNumPrime;
  for (int i = 2; i <= n; i++)
  {
    isNumPrime = isPrime(i);
    if (isNumPrime)
    {
      printf("%d ", i);
    }
  }
  printf("\n");
  return 0;
}
