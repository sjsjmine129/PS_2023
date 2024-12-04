#include <stdio.h>
#include <string.h>

#define MAX_WORDS 10000
#define WORD_LENGTH 4


const char *numWords[] = {"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};


int getNumber(const char *word) {
    for (int i = 0; i < 10; i++) {
        if (strcmp(word, numWords[i]) == 0) {
            return i;
        }
    }
    return -1; 
}


const char* getWord(int number) {
    return numWords[number];
}

int main(void) {
    int T;  
    setbuf(stdout, NULL);  

    scanf("%d", &T);
    for (int test_case = 1; test_case <= T; test_case++) {
        int N;  
        char testNumber[10]; 

        scanf("%s %d", testNumber, &N);

        char words[MAX_WORDS][WORD_LENGTH];
        int numbers[MAX_WORDS]; 


        for (int i = 0; i < N; i++) {
            scanf("%s", words[i]);
            numbers[i] = getNumber(words[i]);  
        }


        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (numbers[i] > numbers[j]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                }
            }
        }

        printf("#%d\n", test_case);
        for (int i = 0; i < N; i++) {
            printf("%s ", getWord(numbers[i]));
        }
        printf("\n");
    }
    return 0;
}
