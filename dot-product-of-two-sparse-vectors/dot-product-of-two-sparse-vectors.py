class SparseVector:
    def __init__(self, nums: List[int]):
        self.locations = dict() # store index : num
        for i in range(len(nums)):
            if nums[i]:
                self.locations[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for index in self.locations:
            if index in vec.locations:
                dot_product += self.locations[index] * vec.locations[index]
        return dot_product

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)