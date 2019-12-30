#include <iostream>

using namespace std;
int d[1001];
int p[1001];
int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> p[i];
	}
	
	for (int i = 1; i <= t; i++) {
		for (int j = 1; j <= i; j++) {
			if (d[i] < d[i - j] + p[j]) {
				d[i] = d[i - j] + p[j];
			}
		}
	}
	cout << d[t];
	return 0;
}