#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long int d[301][3];

int main() {
	int n;
	cin >> n;
	vector<int> a(n+1);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	d[1][1] = a[1];
	for (int i = 2; i <= n; i++) {
		d[i][1] = max(d[i - 2][1], d[i - 2][2]) + a[i];
		d[i][2] = d[i - 1][1] + a[i];
	}
	cout << max(d[n][1], d[n][2]);

	return 0;
}