#include <iostream>

using namespace std;



void naturalSum(int a,int b, int count) {
	int start = b;
	cout << start << endl;

	int result = 0;
	while (start <= a) {
		result += start;
		start++;
		cout << "result :" << result << endl;
		cout << "count: " << count << endl;
		if (result == a) {
			count++;
			naturalSum(a, b + 1, count);
		}
		else if (result > a) {
		
			naturalSum(a, b + 1, count);
		}
	}

}
int main() {
	int T,n;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> n;
		naturalSum(n,1,0);
	}
	return 0;
}