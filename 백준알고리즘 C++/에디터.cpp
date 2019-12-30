#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	stack<char> st_left;
	stack<char> st_right;
	int n;
	string s;
	char s2;
	char command;
	cin >> s;
	for (int i = 0; i < s.size(); i++) {
		st_left.push(s[i]);
	}
	cin >> n;

	while (n--) {
		cin >> command;
		if (command == 'P') {
			cin >> s2;
			st_left.push(s2);
		}
		
		if (command == 'L') {
			if (!st_left.empty()) {
			st_right.push(st_left.top());
			st_left.pop();
			}
		}
		if (command == 'D') {
			if (!st_right.empty()) {
				st_left.push(st_right.top());
				st_right.pop();
			}
		}
		if (command == 'B') {
			if (!st_left.empty()) {
				st_left.pop();
			}
		}
		
	}
	while (!st_left.empty()) {
		st_right.push(st_left.top());
		st_left.pop();
	}
	while (!st_right.empty()) {
		cout << st_right.top();
		st_right.pop();
	}
	
	
	return 0;
}