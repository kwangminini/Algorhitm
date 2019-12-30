#include <iostream>

using namespace std;
long long d[100][1];
int main() {
	int n;
	cin >> n;
	d[2][0] = 1;
	for (int i = 3; i <= n; i++) {
		d[i][0] = d[i - 1][0] + d[i - 1][1];
		d[i][1] = d[i - 1][0];
	}
	cout << d[n][0] + d[n][1];
	return 0;

}
/*
long long d[100];
int main() {
	int n;
	cin >> n;
	d[1] = 1;
	d[2] = 1;
	for (int i = 3; i <= n; i++) {
		d[i] = d[i - 1] + d[i - 2];
	}
	cout << d[n];
	return 0;
}*/