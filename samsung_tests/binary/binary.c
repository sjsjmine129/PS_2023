#include <stdio.h>
#define MAXROW 50
#define MAXCOL 100
#define CODELEN 7 * 8
 
char input[MAXROW][MAXCOL];
char code[CODELEN];
char decrypt[127] = { 0, };
int isFirst = 1;
 
void makeDecrypt() {
    isFirst = 0;
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
int verification(char arr[CODELEN]) {
 
    int decimal[8] = { 0, };
    int dIdx = 0;
 
    for (int i = 0; i < CODELEN; i++) {
        if (i != 0 && i % 7 == 0) {
            decimal[dIdx] = decrypt[decimal[dIdx]];
            dIdx++;
        }
        decimal[dIdx] <<= 1;
        decimal[dIdx] += (arr[i] - '0');
    }
    decimal[dIdx] = decrypt[decimal[dIdx]];
    int odd = 0;    //홀수
    int even = 0;   //짝수
    int sum = 0;
    for (int i = 0; i < 8; i++) {
        if (i % 2 == 1)
            odd += decimal[i];
        else
            even += decimal[i];
        sum += decimal[i];
    }
 
    if (((even * 3) + odd) % 10 == 0)
        return sum;
    return 0;
}
 
int main(void)
{
    int test_case;
    int T;
    int n, m;
    int result;
    int row, col;
    int flag;
 
    setbuf(stdout, NULL);
    scanf("%d", &T);
    isFirst = 1;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        result = 0;
        if (isFirst)
            makeDecrypt();
        flag = 0;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", input[i]);
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (input[i][j] == '1') {
                    row = i;
                    col = j - CODELEN + 1;
                    flag = 1;
                    break;
                }
                if (flag) break;
            }
            if (flag) break;
        }
        for (int i = 0; i < CODELEN; i++) {
            code[i] = input[row][col + i];
        }
        result = verification(code);
 
        printf("#%d %d\n", test_case, result);
    }
    return 0;
}