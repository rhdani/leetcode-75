def merge_sorted(nums1, m, nums2, n):
    global last_merge_result
    
    if (n == 0):
        last_merge_result = nums1
        return nums1
    if (m == 0):
        #Copy nums2 to num1
        for i in range(n):
            nums1[i] = nums2[i]
        last_merge_result = nums1
        return nums1
    
    nums1_index = m - 1 
    nums2_index = n - 1
    output_index = m + n - 1
    
    while (nums2_index >= 0 and nums1_index >= 0):
        if (nums2[nums2_index] > nums1[nums1_index]):
            nums1[output_index] = nums2[nums2_index]
            nums2_index -= 1
        else:
            nums1[output_index] = nums1[nums1_index]
            nums1_index -= 1
        output_index -= 1
    
    while (nums2_index >= 0):
        nums1[output_index] = nums2[nums2_index]
        nums2_index -= 1
        output_index -= 1
    
    
    last_merge_result = nums1
    return nums1

# store last merge result for testing
last_merge_result = None

# Driver code
def main():
    m = [9, 2, 3, 1, 8]
    n = [6, 1, 4, 2, 1]
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0], [1, 2, 0], [1, 1, 1, 0, 0, 0, 0], [6, 0, 0], [12, 34, 45, 56, 67, 78, 89, 99, 0]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]
    expected = [
        [23, 32, 33, 35, 41, 44, 47, 49, 50, 51, 56, 61, 91, 99, 105],
        [1, 2, 7],
        [1, 1, 1, 1, 2, 3, 4],
        [-99, -45, 6],
        [12, 34, 45, 56, 67, 78, 89, 99, 100]
    ]
    k = 1
    for i in range(len(m)):
        print(k, ".\tnums1: ", nums1[i], ", m: ", m[i], sep = "")
        print("\tnums2: ", nums2[i], ", n: ", n[i], sep = "")
        print("\n\tMerged list: ", merge_sorted(nums1[i], m[i], nums2[i], n[i]), sep = "")
        print("-"*100, "\n")
        # validate last merge result using assert and report Pass/Fail
        res = last_merge_result
        try:
            assert res == expected[i]
            print("\tTest Result: Pass")
        except AssertionError:
            print("\tTest Result: Fail")

        k += 1


if __name__ == "__main__":
    main()
