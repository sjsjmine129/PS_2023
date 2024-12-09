#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
 
vector<pair<int, int>> result;
vector<int> subSumArr;
int counter;
 
string change(int l, int r, string str) {
    int s = l, e = r;
    while (l < r) {
        char temp = str[l];
        str[l] = str[r];
        str[r] = temp;
        l++; r--;
    }
 
    for(int i=s; i<=e; i++){
        if (str[i] == '(') str[i] = ')';
        else if (str[i] == ')') str[i] = '(';
    }
 
    return str;
}
 
string flip(string str, int length) {
    int min = 0;
    int position = -1;
    int ret = 0;
    for (int i = 0; i < length; i++) {
        if (str[i] == '(') ret++;
        else if (str[i] == ')') ret--;
 
        if (ret < min) {
            min = ret; 
            position = i; 
        }
    }
 
    if (position != -1) {
        counter++;
        result.push_back(make_pair(0, position));
        str = change(0, position, str);
    }
 
    return str;
}
 
void solve(string str, int len) {
    if (len % 2 == 1) {
        counter = -1;
        return;
    }
 
    str = flip(str, len);
 
    int sum = 0;
    for (int i = 0; i < len; i++) {
        if (str[i] == '(') sum++;
        else if (str[i] == ')') sum--;
        subSumArr.push_back(sum);
    }
 
    if(subSumArr.back() == 0) return;
    
    int halfValue = subSumArr.back() / 2;
    int pos = -1;
    for (int i = 0; i < len; i++) {
        if (halfValue == subSumArr.at(i)) {
            pos = i + 1;
        }
    }
    result.push_back(make_pair(pos, len - 1));
    counter++;
}
 
int main(void) {
    int testCase;
    cin >> testCase;
    for (int tc = 1; tc <= testCase; tc++) {
        int len; string str;
        cin >> len >> str;
        
        counter = 0;
        subSumArr.clear();
        result.clear();
 
        solve(str, len);
 
        printf("#%d %d\n", tc, counter);
        for (int i = 0; i < result.size(); i++) {
            printf("%d %d\n", result[i].first, result[i].second);
        }
    }
    return 0;
}