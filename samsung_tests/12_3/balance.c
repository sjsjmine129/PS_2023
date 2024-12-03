#include <stdio.h>
#include <math.h>

// 힘 계산 함수
double calculate_force(double x, int num_magnets, double positions[], double masses[], int direction) {
    double force = 0.0;
    for (int i = 0; i < num_magnets; i++) {
        double distance = fabs(x - positions[i]);
        if (direction == 0 && x > positions[i]) { // 왼쪽 힘 계산
            force += masses[i] / (distance * distance);
        }
        else if (direction == 1 && x < positions[i]) { // 오른쪽 힘 계산
            force += masses[i] / (distance * distance);
        }
    }
    return force;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; ++test_case) {
        int N;
        scanf("%d", &N);

        double positions[10], masses[10];
        for (int i = 0; i < N; i++) {
            scanf("%lf", &positions[i]);
        }
        for (int i = 0; i < N; i++) {
            scanf("%lf", &masses[i]);
        }

        printf("#%d", test_case);
        // 각 자성체 사이의 균형점 계산
        for (int i = 0; i < N - 1; i++) {
            double left = positions[i];
            double right = positions[i + 1];
            double mid;

            // 이분 탐색
            while (right - left > 1e-12) {
                mid = (left + right) / 2;
                double force_left = calculate_force(mid, N, positions, masses, 0);
                double force_right = calculate_force(mid, N, positions, masses, 1);

                // 힘 비교
                if (force_left > force_right) {
                    left = mid;
                } else {
                    right = mid;
                }
            }

            // 결과 출력 (소수점 10자리)
            printf(" %.10lf", mid);
        }
        printf("\n");
    }
    return 0;
}
