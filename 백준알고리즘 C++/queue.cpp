#include <iostream>
#include <string>
#define MAX_SIZE 10000
using namespace std;

struct que {
	int end_point=0;
	int begin = 0;
	int queu[MAX_SIZE];
};
void que_push(int n,que * que) {
	que->queu[que->end_point] = n;
	que->end_point++;
}
void que_pop(que * que) {
	if (que->end_point - que->begin != 0) {
		cout << que->queu[que->begin]<< endl;
		que->queu[que->begin] = 0;
		que->begin++;
	}
	else {
		cout << "-1" << endl;
	}
}
void que_size(que * que) {
	cout << que->end_point - que->begin << endl;
}
void que_empty(que * que) {
	if (que->end_point - que->begin == 0) {
		cout << "1" << endl;
	}
	else
		cout << "0" << endl;
}
void que_front(que * que) {
	if (que->end_point - que->begin != 0)
		cout << que->queu[que->begin] << endl;
	else
		cout << "-1" << endl;
}
void que_back(que * que) {
	if (que->end_point - que->begin != 0)
		cout << que->queu[(que->end_point)-1] << endl;
	else
		cout << "-1" << endl;
}

int main() {
	string s;
	que q;
	int point;
	int n,num;
	cin >> n;
	while (n--) {
		cin >> s;
		if (s == "push") {
			cin >> num;
			que_push(num, &q);
		}
		if (s == "pop") {
			que_pop(&q);
		}
		if (s == "size") {
			que_size(&q);
		}
		if (s == "empty") {
			que_empty(&q);
		}
		if (s == "front") {
			que_front(&q);
		}
		if (s == "back") {
			que_back(&q);
		}
	}
	
	return 0;
}