#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

#define forloop(n) for (int i = n; i--;)
#define rightshift(n, m) (n) >> (m)
#define xor(n, m) (n) ^ (m)

void main(void) {
    int i = rand();
    int k = 13;
    int e;
    int * p = & i;

    printf("%d\n", i);
    fflush(stdout);
    scanf("%d %d", & k, & e);

    forloop(7)
        k = rightshift(* p, k % 3);

    k = xor(k, e);

    if(k == 53225)
        puts(Fahne);
    else
        puts("War wohl void!");
}
