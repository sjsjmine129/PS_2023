#include <stdio.h>

int main(void) {
    int T;
    scanf("%d", &T);  // 테스트 케이스 수 입력

    for (int test_case = 1; test_case <= T; ++test_case) {
        int N;
        scanf("%d", &N);  // 건물 개수 입력

        int buildings[N];
        for (int i = 0; i < N; i++) {
            scanf("%d", &buildings[i]);  // 건물 높이 입력
        }

        int view_count = 0;

        // 양쪽 두 칸에는 건물이 없으므로, 인덱스 2부터 N-3까지 검사
        for (int i = 2; i < N - 2; i++) {
            int left_max = (buildings[i - 2] > buildings[i - 1]) ? buildings[i - 2] : buildings[i - 1];
            int right_max = (buildings[i + 1] > buildings[i + 2]) ? buildings[i + 1] : buildings[i + 2];
            
            int max_adjacent = (left_max > right_max) ? left_max : right_max;

            // 현재 건물이 주변 최대 높이보다 2 이상 높을 경우
            if (buildings[i] > max_adjacent) {
                view_count += buildings[i] - max_adjacent;
            }
        }

        // 결과 출력
        printf("#%d %d\n", test_case, view_count);
    }

    return 0;
}
