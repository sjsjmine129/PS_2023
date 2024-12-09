#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
 
int flipCnt;
vector<pair<int, int>> result;
vector<int> subSumArr;
 
string rOperation(int left, int right, string str) {
    int s = left, e = right;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++; right--;
    }
 
    for(int i=s; i<=e; i++){
        if (str[i] == '(') str[i] = ')';
        else if (str[i] == ')') str[i] = '(';
    }
 
    return str;
}
 
string flip(string str, int len) {
    int minValue = 0, pos = -1, sum = 0;
    for (int i = 0; i < len; i++) {
        if (str[i] == '(') sum++;
        else if (str[i] == ')') sum--;
 
        if (sum < minValue) {
            minValue = sum; // 음수이면서 제일 작은 값으로 갱신
            pos = i; // 인덱스
        }
    }
 
    // 누적합이 음수인 경우가 존재하였다면
    if (pos != -1) {
        flipCnt++;
        result.push_back(make_pair(0, pos));
        str = rOperation(0, pos, str);
    }
 
    return str;
}
 
void solve(string str, int len) {
    if (len % 2 == 1) {
        flipCnt = -1;
        return;
    }
 
    // 각 구간합 원소가 음수가 없도록 처리
    str = flip(str, len);
 
    // 구간 누적합
    int sum = 0;
    for (int i = 0; i < len; i++) {
        if (str[i] == '(') sum++;
        else if (str[i] == ')') sum--;
        subSumArr.push_back(sum);
    }
 
    if(subSumArr.back() == 0) return;
    
    // 누적합의 절반값을 가지는 누적합들 중 가장 마지막 인덱스 찾기
    int halfValue = subSumArr.back() / 2;
    int pos = -1;
    for (int i = 0; i < len; i++) {
        if (halfValue == subSumArr.at(i)) {
            pos = i + 1;
        }
    }
    result.push_back(make_pair(pos, len - 1));
    flipCnt++;
}
 
int main(void) {
    int testCase;
    cin >> testCase;
    for (int tc = 1; tc <= testCase; tc++) {
        int len; string str;
        cin >> len >> str;
        
        flipCnt = 0;
        subSumArr.clear();
        result.clear();
 
        solve(str, len);
 
        printf("#%d %d\n", tc, flipCnt);
        for (int i = 0; i < result.size(); i++) {
            printf("%d %d\n", result[i].first, result[i].second);
        }
    }
    return 0;
}