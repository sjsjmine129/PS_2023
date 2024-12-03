#include <stdio.h>

#define SIZE 100

int main(void) {
    int T = 10;
    
    for (int test_case = 1; test_case <= T; ++test_case) {
        int n;
        scanf("%d", &n);
        
        int table[SIZE][SIZE]; 

        for (int i = 0; i < SIZE; ++i) {
            for (int j = 0; j < SIZE; ++j) {
                scanf("%d", &table[i][j]);
            }
        }
        
        int count = 0;
        for (int col = 0; col < SIZE; ++col) {
            int magnetic = 0;
            
            for (int row = 0; row < SIZE; ++row) {
                if (table[row][col] == 1) {
                    magnetic = 1;
                } else if (table[row][col] == 2 && magnetic) {
                    count++;
                    magnetic = 0;
                }
            }
        }
        
        printf("#%d %d\n", test_case, count);
    }
    return 0;
}
