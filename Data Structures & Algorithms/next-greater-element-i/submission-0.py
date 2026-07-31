class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        nge = {}

        for i in range(len(nums2)-1,-1,-1):
            current = nums2[i]

            while stack and stack[-1] <=current:
                stack.pop()

            if not stack:
                nge[current] = -1
            else:
                nge[current] = stack[-1]

            stack.append(current)

        ans = []

        for num in nums1:
            ans.append(nge[num])

        return ans