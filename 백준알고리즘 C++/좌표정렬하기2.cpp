#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	vector<pair<int, int>> p(n);
	for (int i = 0; i < n; i++) {
		cin >> p[i].second >> p[i].first;
	}
	sort(p.begin(), p.end());
	for (int i = 0; i < p.size(); i++) {
		cout << p[i].second << " " << p[i].first << "\n";
	}
	
	return 0;
}