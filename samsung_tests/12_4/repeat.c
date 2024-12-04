#include <stdio.h>
#include <string.h>

#define SIZE 8  

int isPalindrome(char *str, int length) {
    for (int i = 0; i < length / 2; i++) {
        if (str[i] != str[length - 1 - i]) {
            return 0;  
        }
    }
    return 1;  
}

int main(void) {
    int test_case;
    int T = 10; 

    setbuf(stdout, NULL);  
    
    for (test_case = 1; test_case <= T; ++test_case) {
        int palindrome_length;
        char board[SIZE][SIZE + 1]; 

        scanf("%d", &palindrome_length); 

        for (int i = 0; i < SIZE; i++) {
            scanf("%s", board[i]);
        }

        int count = 0;

        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j <= SIZE - palindrome_length; j++) {
                if (isPalindrome(&board[i][j], palindrome_length)) {
                    count++;
                }
            }
        }

        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j <= SIZE - palindrome_length; j++) {
                char temp[SIZE]; 
                for (int k = 0; k < palindrome_length; k++) {
                    temp[k] = board[j + k][i];
                }
                if (isPalindrome(temp, palindrome_length)) {
                    count++;
                }
            }
        }

        printf("#%d %d\n", test_case, count);
    }

    return 0;
}
