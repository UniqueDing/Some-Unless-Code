#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

//vector<int> ori {0, 1, 8, 22, 35, 2, 9, 6};
vector<int> ori {0, 1, 8, 22, 2, 9, 35, 6};
int n = ori.size() - 1;

void heap_sort (vector<int>& tmp, int start)
{
	if (start > n)
	{
		return;
	}

	// 大于就进行交换，小于不用
//	if (ori[start] < ori[start * 2])
//	{
//		// 不用交换
//	}

	int left = start * 2;
	int right = start * 2 + 1;
	int tm_node;

	// left node
	if ( ori[left] != 0 && ori[start] > ori[left])
	{
		if (ori[right] != 0 && ori[right] < ori[left])
		{
			// have right node && right < left
		}

	}

	// right node
	return;
}
int main(void)
{
	ostream_iterator<int, char> out(cout, " ");

	cout << "before:" << endl;
	copy(ori.begin(), ori.end(), out);
	cout.put('\n');

	cout << "after: " << endl;
	heap_sort(ori, 1);
	copy(ori.begin(), ori.end(), out);
	cout.put('\n');
	

	return 0;
}
