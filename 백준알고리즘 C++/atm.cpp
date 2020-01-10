#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n,result=0;
	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	sort(v.begin(),v.end());
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			result += v[j];
		}
	}
	cout << result;
	return 0;
}