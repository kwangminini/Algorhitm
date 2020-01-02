#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, h,result=1;
	cin >> n >> h;
	vector<int> v(n);
	vector<int> count(h);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	for (int i = 1; i <= 5; i++) {
		for (int j = 0; j < n; j = j + 2) {
			if (v[j] >= i) {
				count[i - 1] += 1;
			}
		}
		for (int l = 1; l < n; l = l + 2) {
			if (v[l]>(h-i)) {
				count[i - 1] += 1;
			}
		}
	}
	sort(count.begin(), count.end());
	for (int i = 0; i < h; i++) {
		if (count[i]==count[i+1]) {
			result += 1;
		}
		else
			break;
	}
	cout << count[0] << " " << result;
	return 0;
}