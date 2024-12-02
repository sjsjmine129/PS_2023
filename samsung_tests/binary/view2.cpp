#include <algorithm>
#include <stdio.h>
#include <iostream>
using namespace std;

int temp[4];
int building[1000];

void feature(int m, int n) {
	int ret = 0;
	for (int i = 2; i<m - 2; ++i) {
		for (int j = 0; j<5; ++j) {
			temp[j] = building[i - 2 + j];
		}
		sort(temp, temp + 5, greater<int>());
		if (building[i] == temp[0]) {
			ret += temp[0] - temp[1];
		}
	}
	printf("#%d %d\n", n, ret);
}

int main() {
	int l;
	for (int i = 0; i<10; ++i) {
		scanf("%d", &l);
		for (int j = 0; j<l; ++j) {
			scanf("%d", &building[j]);
		}
		feature(l, i + 1);
	}
	return 0;
}