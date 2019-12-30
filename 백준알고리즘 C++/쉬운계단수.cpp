#include <iostream>

using namespace std;

long long mod = 1000000000;
long long d[101][10];
int main() {
	int n;
	long long result=0;
	cin >> n; 
	for (int i = 1; i < 10; i++) {
		d[1][i] = 1;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j <= 9; j++) {
			d[i][j] = 0;
			if (j - 1 >= 0) {
				d[i][j] += d[i - 1][j - 1];
			}
			if (j + 1 <= 9) {
				d[i][j] += d[i - 1][j + 1];
			}
			d[i][j] %= mod;
		}
	}
	for (int i = 0; i < 10; i++) {
		result += d[n][i];
	}
	cout << result % mod;

	return 0;
}