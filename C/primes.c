#include <stdio.h>
#include <stdbool.h>

// PRIME NUMBERS

bool Is_Prime(int n){

    if (n < 2){
        return false;
    }

    if (n == 2){
        return true;
    }

    if (n % 2 == 0) {
        return false;
    }

    for (int i = 3; i * i <= n; i+=2) {
        if (n % i == 0){
            return false;
        }
    }

    return true;
}

int main() {
    int limit = 0;
    int count = 0;
    printf("Find primes up to: ");
    scanf("%d", &limit);
    
    printf("Prime numbers up to %d:\n", limit);
    for (int i = 2; i <= limit; i++) {
        if (Is_Prime(i)) {
            printf("%d ", i);
            count ++;
        }
    }
    printf("\n");
    printf("There are %d number of Primes upto %d\n",count,limit);
    
    return 0;
}