#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int max_value;
int visited[1000000][11]; // Array to store visited states (number and remaining swaps)

// Swap two characters
void swap(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Recursive function with memoization
void find_max(char num[], int k, int len) {
    if (k == 0) { // Base case: No swaps left
        int value = atoi(num);
        if (value > max_value) {
            max_value = value;
        }
        return;
    }
    
    int value = atoi(num);
    if (visited[value][k]) return; // Skip if this state has been visited
    visited[value][k] = 1;
    
    // Try all pairs of swaps
    for (int i = 0; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            swap(&num[i], &num[j]);
            find_max(num, k - 1, len); // Recur with one less swap
            swap(&num[i], &num[j]); // Undo the swap
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    
    for (int test_case = 1; test_case <= T; test_case++) {
        char num[7]; // Up to 6 digits
        int k;
        scanf("%s %d", num, &k);
        
        int len = strlen(num);
        max_value = 0;
        memset(visited, 0, sizeof(visited)); // Reset visited states for each test case
        
        find_max(num, k, len);
        printf("#%d %d\n", test_case, max_value);
    }
    return 0;
}