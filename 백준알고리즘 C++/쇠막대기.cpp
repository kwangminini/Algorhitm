#include <iostream>
#include <string>
#include <stack>
using namespace std;


int main() {
	string s;
	cin >> s;
	stack<int> s1;
	int n = s.size();
	int count=0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '(') {
			s1.push(i);
		}
		else {
			if ((i-s1.top())==1)
			{
				s1.pop();
				count += s1.size();
			}
			else {
				s1.pop();
				count += 1;
			}

		}
	}
	cout << count << endl;
	return 0;
}