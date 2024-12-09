#include <iostream>
#include <vector>
#include <string>
using namespace std;

int flipCount;
vector<pair<int, int>> operations;
vector<int> cumulativeSumArray;

string reverseAndFlip(int start, int end, string str) {
    int left = start, right = end;
    while (left < right) {
        swap(str[left], str[right]);
        left++;
        right--;
    }

    for (int i = start; i <= end; i++) {
        str[i] = (str[i] == '(') ? ')' : '(';
    }

    return str;
}

string ensureNonNegativePrefixSum(string str, int length) {
    int minPrefixSum = 0, minIndex = -1, currentSum = 0;

    for (int i = 0; i < length; i++) {
        currentSum += (str[i] == '(') ? 1 : -1;

        if (currentSum < minPrefixSum) {
            minPrefixSum = currentSum;
            minIndex = i;
        }
    }

    if (minIndex != -1) {
        flipCount++;
        operations.emplace_back(0, minIndex);
        str = reverseAndFlip(0, minIndex, str);
    }

    return str;
}

void solve(string str, int length) {
    if (length % 2 != 0) {
        flipCount = -1;
        return;
    }

    str = ensureNonNegativePrefixSum(str, length);

    int currentSum = 0;
    for (int i = 0; i < length; i++) {
        currentSum += (str[i] == '(') ? 1 : -1;
        cumulativeSumArray.push_back(currentSum);
    }

    if (cumulativeSumArray.back() == 0) return;

    int targetSum = cumulativeSumArray.back() / 2;
    int splitIndex = -1;

    for (int i = 0; i < length; i++) {
        if (cumulativeSumArray[i] == targetSum) {
            splitIndex = i + 1;
        }
    }

    operations.emplace_back(splitIndex, length - 1);
    flipCount++;
}

int main() {
    int testCases;
    cin >> testCases;

    for (int t = 1; t <= testCases; t++) {
        int length;
        string sequence;

        cin >> length >> sequence;

        flipCount = 0;
        cumulativeSumArray.clear();
        operations.clear();

        solve(sequence, length);

        cout << "#" << t << " " << flipCount << "\n";
        for (const auto& op : operations) {
            cout << op.first << " " << op.second << "\n";
        }
    }

    return 0;
}
