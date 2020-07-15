#include <stdio.h>

void swap(int *p, int *q)
{
	int temp = *p;
	*p = *q;
	*q = temp;
	/* int *temptr = *p; */
	/* *p = *q; */
	/* *q = temptr; */
}

void quick_sort(int l[], int start, int end)
{
	if(start >= end)
		return;
	int *p = &l[start];
	int *q = &l[end];
	int **m = &p;

	while(p != q){
		if (*m == p){
			if(*p > *q){
				swap(p, q);
				p++;
				m = &q;
			}else{
				q--;
			}
		}else{
			if(*p > *q){
				swap(p, q);
				q--;
				m = &p;
			}else{
				p++;
			}
		}
	}
 	quick_sort(l, start, (*m - &l[0]));
	quick_sort(l, (*m - &l[0]) + 1, end);
}

int main()
{
	int l[8] = {7, 3, 19, 3, 44, 22, 6, 13};
	quick_sort(l, 0, sizeof(l) / sizeof(int) - 1);
	for(int i = 0; i < sizeof(l) / sizeof(int); i++){
		printf("%d ", l[i]);
	}
}
