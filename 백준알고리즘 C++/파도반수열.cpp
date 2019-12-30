#include <iostream>
using namespace std;

int main() {
	int t,n;
	long long int arr[101] = { 0,1,1,1,2,2 };
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		if (n > 5) {
			for (int i = 6; i <= n;i++) {
				arr[i] = arr[i - 1] + arr[i - 5];
			}
			cout << arr[n]<<'\n';
		}
		else
			cout << arr[n]<<'\n';
	}

	return 0;
}