#include <stdio.h>
#include <math.h>

// 조합 계산 함수
double combination(int n, int r) {
    double res = 1;
    for (int i = 1; i <= r; i++) {
        res *= (n - i + 1) / (double)i;
    }
    return res;
}

// 소수인지 확인하는 함수
int is_prime(int num) {
    if (num < 2) return 0;
    if (num == 2) return 1;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; ++test_case) {
        int skillA, skillB;
        scanf("%d %d", &skillA, &skillB);
        
        double pA = skillA / 100.0;
        double pB = skillB / 100.0;
        double total_prob = 0;

        // 소수 배열
        int primes[] = {2, 3, 5, 7, 11, 13, 17};

        // A 또는 B의 소수 완제품 확률 계산
        for (int i = 0; i <= 18; i++) {
            for (int j = 0; j <= 18; j++) {
                int primeA = is_prime(i);
                int primeB = is_prime(j);
                if (primeA || primeB) {
                    double probA = combination(18, i) * pow(pA, i) * pow(1 - pA, 18 - i);
                    double probB = combination(18, j) * pow(pB, j) * pow(1 - pB, 18 - j);
                    total_prob += probA * probB;
                }
            }
        }

        printf("#%d %.6f\n", test_case, total_prob);
    }
    return 0;
}
