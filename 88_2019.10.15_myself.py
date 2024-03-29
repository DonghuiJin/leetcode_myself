'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m - 1] <= nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
if __name__ == '__main__':
    t1 = [1, 2, 3, 0, 0, 0]
    t1_size = 3
    t2 = [2, 5, 6]
    t2_size = 3
    merge(t1, t1_size, t2, t2_size)
    print(t1)






















