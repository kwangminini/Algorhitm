#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

struct Person {
	int age;
	string name;
};
bool cmp(const Person &u, const Person &v) {
	if (u.age < v.age) {
		return true;
	}
	else
		return false;
}
int main() {
	int n;
	cin >> n;
	vector<Person> p(n);
	for (int i = 0; i < n; i++) {
		cin >> p[i].age >> p[i].name;
	}
	stable_sort(p.begin(), p.end(),cmp);
	for (int i = 0; i < n; i++) {
		cout << p[i].age << " " << p[i].name << "\n";
	}
	return 0;
}