#include <stdio.h>


char data[50][100];
char code[56];
char decrypt[127] = {0};

void makeDecrypt() {
    for (int i = 0; i < 127; i++)
        decrypt[i] = 0;

    decrypt[13] = 0;
    decrypt[25] = 1;
    decrypt[19] = 2;
    decrypt[61] = 3;
    decrypt[35] = 4;
    decrypt[49] = 5;
    decrypt[47] = 6;
    decrypt[59] = 7;
    decrypt[55] = 8;
    decrypt[11] = 9;
}

int verification(char arr[56]) {
    int decimal[8] = {0};
    int dIdx = 0;

    for (int i = 0; i < 56; i++) {
        if (i % 7 == 0 && i != 0) {
            decimal[dIdx] = decrypt[decimal[dIdx]];
            dIdx++;
        }
        decimal[dIdx] <<= 1;
        decimal[dIdx] += (arr[i] - '0');
    }
    decimal[dIdx] = decrypt[decimal[dIdx]];

    int odd_sum = 0;
    int even_sum = 0;
    int total_sum = 0;

    for (int i = 0; i < 8; i++) {
        if (i % 2 == 0)
            even_sum += decimal[i];
        else
            odd_sum += decimal[i];
        total_sum += decimal[i];
    }

    return (((even_sum * 3) + odd_sum) % 10 == 0) ? total_sum : 0;
}

int findCodeStart(int n, int m, int *row, int *col) {
    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (data[i][j] == '1') {
                *row = i;
                *col = j - 56 + 1;
                return 1;
            }
        }
    }
    return 0;
}

void extractCode(int row, int col) {
    for (int i = 0; i < 56; i++) {
        code[i] = data[row][col + i];
    }
}

int main(void) {
    int T;
    scanf("%d", &T);
    makeDecrypt(); 

    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, m;
        int result = 0;
        scanf("%d %d", &n, &m);

        // Read the data grid
        for (int i = 0; i < n; i++) {
            scanf("%s", data[i]);
        }

        int row, col;
        if (findCodeStart(n, m, &row, &col)) {
            extractCode(row, col);      
            result = verification(code);  
        }

        printf("#%d %d\n", test_case, result);
    }

    return 0;
}
