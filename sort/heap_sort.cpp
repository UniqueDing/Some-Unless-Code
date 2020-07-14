#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;


vector<int> arr{1, 8, 22, 2, 9, 35, 6};
int n = arr.size();
int flag = 0;

void to_down(vector<int> &tmp, int start) {
	if (flag == 1) {
		flag = 0;
		return;
	}

	int left = start * 2 + 1;
	int right = left + 1;
	int tmp_node = start;

	if (arr[left] != 0 && arr[left] < arr[start]) {
		tmp_node = left;
	}
	if (arr[right] != 0 && arr[right] < arr[tmp_node]) {
		tmp_node = right;
	}

	if (start == tmp_node) {
		flag = 1;
		return;
	}
	swap(arr[start], arr[tmp_node]);
}

void init_heap(vector<int> &tmp) {
	for (int i = (n / 2) - 1; i >= 0; --i) {
		to_down(arr, i);
	}
}

void heap_sort (void)
{
	while (n >= 0)
	{
		swap(arr[1], arr[n]);
		to_down(arr, 0);
//		cout << arr[n] << " ";
		n --;
	}
//	cout.put('\n');
}


int main(void) {
	ostream_iterator<int, char> out(cout, " ");

	copy(arr.begin(), arr.end(), out);
	cout.put('\n');

	init_heap(arr); // 建堆
	copy(arr.begin(), arr.end(), out);
	cout.put('\n');

	heap_sort();
	copy(arr.begin(), arr.end(), out);
	cout.put('\n');
	return 0;
}
