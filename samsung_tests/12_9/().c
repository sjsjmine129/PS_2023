#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

// Global variables for flip count, result pairs, and prefix sums
int flipCount;
vector<pair<int, int>> operations;
vector<int> prefixSum;

string reverseAndFlip(int start, int end, string str) {
    int left = start, right = end;
    // Reverse the substring
    while (left < right) {
        swap(str[left], str[right]);
        left++;
        right--;
    }

    // Flip parentheses
    for (int i = start; i <= end; i++) {
        if (str[i] == '(') str[i] = ')';
        else if (str[i] == ')') str[i] = '(';
    }

    return str;
}

string balancePrefix(string str, int length) {
    int minBalance = 0, imbalanceIndex = -1, currentBalance = 0;

    // Find the position of maximum imbalance
    for (int i = 0; i < length; i++) {
        if (str[i] == '(') currentBalance++;
        else if (str[i] == ')') currentBalance--;

        if (currentBalance < minBalance) {
            minBalance = currentBalance;
            imbalanceIndex = i;
        }
    }

    // If imbalance exists, perform a flip operation
    if (imbalanceIndex != -1) {
        flipCount++;
        operations.push_back({0, imbalanceIndex});
        str = reverseAndFlip(0, imbalanceIndex, str);
    }

    return str;
}

void solveParentheses(string str, int length) {
    if (length % 2 != 0) {
        // Unbalanced case
        flipCount = -1;
        return;
    }

    // Balance the prefix
    str = balancePrefix(str, length);

    int totalBalance = 0;

    // Calculate prefix sums
    for (int i = 0; i < length; i++) {
        if (str[i] == '(') totalBalance++;
        else if (str[i] == ')') totalBalance--;
        prefixSum.push_back(totalBalance);
    }

    // If balanced, no additional operations needed
    if (prefixSum.back() == 0) return;

    // Find the position where half of the total imbalance is corrected
    int halfImbalance = prefixSum.back() / 2;
    int splitIndex = -1;

    for (int i = 0; i < length; i++) {
        if (prefixSum[i] == halfImbalance) {
            splitIndex = i + 1;
            break;
        }
    }

    // Perform the second flip operation
    operations.push_back({splitIndex, length - 1});
    flipCount++;
}

int main() {
    int testCases;
    cin >> testCases;

    for (int testCase = 1; testCase <= testCases; testCase++) {
        int length;
        string inputStr;
        cin >> length >> inputStr;

        // Reset global variables for each test case
        flipCount = 0;
        prefixSum.clear();
        operations.clear();

        // Solve the current test case
        solveParentheses(inputStr, length);

        // Print results
        cout << "#" << testCase << " " << flipCount << endl;
        for (const auto& operation : operations) {
            cout << operation.first << " " << operation.second << endl;
        }
    }

    return 0;
}
