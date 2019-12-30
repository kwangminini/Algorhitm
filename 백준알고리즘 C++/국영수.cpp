#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
struct Person{
	string name;
	int korean, math, english;
};
bool cmp(const Person &u, const Person &v){
	if (u.korean > v.korean)
		return true;
	else if (u.korean == v.korean) {
		if (u.english < v.english) {
			return true;
		}
		else if (u.english == v.english) {
			if (u.math > v.math) {
				return true;
			}
			else if (u.math == v.math) {
				return u.name < v.name;
			
			}
			
		}
		
	}
	return false;
}
int main() {
	int n;
	cin >> n;
	vector<Person> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i].name >> v[i].korean >> v[i].english >> v[i].math;
	}
	stable_sort(v.begin(), v.end(), cmp);
	for (int i = 0; i < n; i++) {
		cout<<v[i].name<<endl;
	}
	return 0;
}