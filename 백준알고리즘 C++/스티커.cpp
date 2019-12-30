#include <iostream>
#include <algorithm>

using namespace std;

long long a[100001][2];
long long d[100001][3];

int _max(int x, int y, int z) {
	if (x >= y) {
		if (x >= z) {
			return x;
		}
		else
			return z;
	}
	else if (y > x) {
		if (y >= z) {
			return y;
		}
		else
			return z;
	}
}
int main() {
	int T, n,k;
	cin >> T;

	while (T--) {
		cin >> n;
		for (int i = 0; i < 2; i++) {
			for (int j = 1; j <= n; j++) {
				cin >> a[j][i];
			}
		}
		d[0][0] = d[0][1] = d[0][2] = 0;
		for (int i = 1; i <= n; i++) {
			d[i][0] = max(d[i - 1][0], max(d[i - 1][1], d[i - 1][2]));
			d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[i][0];
			d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[i][1];
		}
		long long result = 0;
		for (int i = 1; i <= n; i++) {
			result = max(max(result, d[i][0]), max(d[i][1], d[i][2]));
		}
		cout << result << endl;
	}
	
	
	return 0;
}