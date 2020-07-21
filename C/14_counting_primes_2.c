#include <stdio.h>
#include <math.h>
#include <stdlib.h>

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

  // dynamically allocating memory for array of size n
  int *arr = malloc(n * sizeof(n + 1));

  for (int i = 2; i < (int)sqrt(n + 1) + 1; i++)
  {
    for (int j = 2; j <= (n + 1) / i; j++)
    {
      arr[i * j] = 1;
    }
  }

  for (int i = 2; i < n + 1; i++)
  {
    if (arr[i] == 0)
      printf("%i ", i);
  }
  printf("\n");

  free(arr); // freeing memory of array

  return 0;
}
