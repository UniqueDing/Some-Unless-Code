#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

//vector<int> arr{1, 8, 22, 2, 9, 35, 6};
//vector<int> arr{8, 35, 6, 9, 22, 2, 1};
//vector<int> arr{42, 28, 3, 8, 23, 12, 2, 34, 24, 1};
vector<int> arr{6, 1, 17, 4, 20, 15, 33, 10, 194, 54, 99, 1004, 5, 477};
int n = arr.size() - 1;
int flag = 0;

void to_down(vector<int> &tmp, int start) {

	int left = start * 2 + 1;
	int right = left + 1;
	int tmp_node = start;

	if (flag == 1) {
		flag = 0;
		return;
	}
	// n 是数组索引
	// > 建立大堆
	// < 建立小堆
	if (left <= n && arr[left] > arr[start]) {
		tmp_node = left;
	}
	if (right <= n && arr[right] > arr[left]) {
		tmp_node = right;
	}

	if (tmp_node == start) {
		flag = 1;
	} else {
		swap(arr[start], arr[tmp_node]);
	}
	to_down(arr, tmp_node);
}

void init_heap(vector<int> &tmp) {
	for (int i = (n / 2); i >= 0; --i) {
		to_down(arr, i);
	}
}

void heap_sort(void) {
	for (int i = arr.size(); i >= 1; i--) {
//		cout << arr[0] << " ";
		swap(arr[0], arr[n]);
		n--;
		to_down(arr, 0);
	}
}


int main(void) {
	ostream_iterator<int, char> out(cout, " ");

	cout << "有元素：" << n << " 个" << endl;
	cout << "未建堆:\n";
	copy(arr.begin(), arr.end(), out);
	cout.put('\n');

	cout << "建堆后：\n";
	init_heap(arr); // 建堆
	copy(arr.begin(), arr.end(), out);
	cout.put('\n');

	cout << "排序后：\n";
	heap_sort();
	copy(arr.begin(), arr.end(), out);
	cout.put('\n');
	return 0;
}
