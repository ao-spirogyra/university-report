#include <stdio.h>
#include <math.h>
#define MAXN 1418092
// a_(n+1) = 1 + 2.0/(1 + a_n)
int main (void) {
  double a = 1;
  for (int n = 1; n <= MAXN; n++) {
    a = 1 + 2.0/(1 + a);
    if ((24<= n && n <= 29) || n == MAXN) {
      printf("n=%d  a=%.18e\n", n,a);
    }
  }
  return 0;
}