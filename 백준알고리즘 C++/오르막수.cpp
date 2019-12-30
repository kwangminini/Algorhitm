#include <iostream>

using namespace std;

long long d[1001][10];
long long mod = 10007;
int main() {
	long long result = 0;
	int n;
	cin >> n;
	for (int i = 0; i < 10; i++)
	{
		d[1][i] = 1;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			for (int z = 0; z <= j; z++) {
				d[i][j] += d[i - 1][z];
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