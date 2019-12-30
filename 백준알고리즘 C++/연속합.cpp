#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	vector<int> d(n);
	for (int i = 0; i < n; i++) {
		d[i] = a[i];
		if (i == 0)continue;
		if (d[i - 1] + a[i] > d[i]) {
			d[i] = d[i - 1] + a[i];
		}
		
	}
	int result = d[0];
	for (int i = 1; i < n; i++) {
		if (result < d[i]) {
			result = d[i];
		}
	}
	cout << result;
	return 0;
}