#include <iostream>

using namespace std;

int d[1000];
int main() {
	int t, n;
	cin >> t;
	d[0] = 1;
	d[1] = 1;
	d[2] = 2;

	for (int i = 0; i < t; i++) {
		cin >> n;
		for (int i = 3; i <= n; i++) {
			d[i] = d[i - 1] + d[i - 2] + d[i - 3];
		}
		cout << d[n] << endl;
	}
	

	return 0;
}