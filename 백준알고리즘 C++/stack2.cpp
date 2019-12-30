#include <iostream>
#include <stack>
#include <string.h>

using namespace std;


int main() {
	stack<int> st;
	int n,num;
	char str[10];
	cin >> n;
	while (n--) {
		cin >> str;
		if (!strcmp(str, "push")) {
			cin >> num;
			st.push(num);
		}
		if (!strcmp(str, "pop")) {
			if (st.empty() == false) {
				cout << st.top() << endl;
				st.pop();
			}
			else
				cout << "-1" << endl;
		}
		if (!strcmp(str, "size")) {
			cout<<st.size()<<endl;
		}
		if (!strcmp(str, "empty")) {
			cout<<(st.empty()?1:0)<<endl;
		}
		if (!strcmp(str, "top")) {
			if (st.empty() == false)
				cout << st.top() << endl;
			else
				cout << "-1" << endl;
		}
	}
	return 0;
}