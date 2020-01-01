#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T, N, res;

typedef struct Pos {
	int x;
	int y;
	Pos(int _x, int _y) :x(_x), y(_y) {};
};

bool check(vector<Pos> v, int x, int y) {
	for (vector<Pos>::iterator i = v.begin(); i != v.end(); i++) {		
		if (x == i->x || y == i->y) return false;
		if (abs(x - i->x) == abs(y - i->y))return false;
	}
	return true;
}

void dp(vector<Pos> v, int x, int y) {
	if (x != N - 1)dp(v, x + 1, y); // �� �����ʺ��� ���� �Ųٷ� ���Ŷ� ���
	if (!check(v, x, y))return; // ���� �� ������ ����
	if (y == N - 1) { // ���Ⱑ ������ ���̸�, ��� +1 �ϰ� ����
		res++;
		return;
	}
	v.push_back(Pos(x, y)); // ���� ���� ��ġ ���Ϳ� �־��ְ�
	dp(v, 0, y + 1); // ���� ��
}

int main()
{
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;

		res = 0;

		vector<Pos> v;
		dp(v, 0, 0);

		cout << "#" << t << " " << res << endl;
	}
}