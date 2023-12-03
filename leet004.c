#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}

int main ()
{
    int nums_a[2] = {1, 3};
    int nums_b[1] = {2};
    int len_a = 2;
    int len_b = 1;
    // int nums_a[2] = {1, 2};
    // int nums_b[2] = {3, 4};
    // int len_a = 2;
    // int len_b = 2;

    double result = findMedianSortedArrays(nums_a, len_a, nums_b, len_b);
    printf("Resultado: %d\n", result);
}