#include <stdio.h>
#include <math.h>
int main (void) {
  double sum;
  for (int i = 0; i < 51; i++) {
    sum = sum + pow(-1,i)/(pow(3,i)*(2*i+1));
    if (i == 10 || i == 30 || i == 50) {
      printf("S_%d = %.16e\n", i, sum*sqrt(12));
    }
  }
  sum = 0;
  for (int i = 30; i > -1 ; i--) {
    sum = sum + pow(-1,i)/(pow(3,i)*(2*i+1));
  }
  printf("S'_30 = %.16e\n", sum*sqrt(12));
  sum = 0;
  for (int i = 10; i > -1 ; i--) {
    sum = sum + pow(-1,i)/(pow(3,i)*(2*i+1));
  }
  printf("S'_10 = %.16e\n", sum*sqrt(12));
  return 0;
}