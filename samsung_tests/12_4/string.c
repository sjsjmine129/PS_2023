#include <stdio.h>
#include <string.h>

int main(void) {
    int test_case;
    int T = 10; 

    setbuf(stdout, NULL); 
    scanf("%d", &T); 

    for (test_case = 1; test_case <= T; ++test_case) {
        char search[11]; 
        char sentence[1001];  

        scanf("%s", search); 
        scanf("%s", sentence);  

        int count = 0;
        int search_len = strlen(search);
        int sentence_len = strlen(sentence);

        for (int i = 0; i <= sentence_len - search_len; i++) {
            int match = 1;
            for (int j = 0; j < search_len; j++) {
                if (sentence[i + j] != search[j]) {
                    match = 0;
                    break;
                }
            }
            if (match) {
                count++;
            }
        }

        printf("#%d %d\n", test_case, count);
    }

    return 0;
}
