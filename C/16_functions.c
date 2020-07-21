#include <stdio.h>

long factorial(int n)
{
  long ans = 1;
  if (n < 1)
  {
    return ans;
  }

  while (n > 1)
  {
    ans *= n;
    n--;
  }
  return ans;
}

int main()
{
  int n;
  printf("Enter number: ");
  scanf("%d", &n);

  printf("factorial of %d is %ld\n", n, factorial(n));
  return 0;
}
