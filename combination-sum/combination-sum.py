class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(combination, current_sum, index):
            # this will add the combination to res array if the sum == target
            if current_sum > target:
                return
            if current_sum == target:
                res.append(combination.copy())
                return
            # current_sum < target:
            for i in range(index, len(candidates)):
                num = candidates[i]
                combination.append(num)
                dfs(combination, current_sum + num, i)
                combination.pop(-1)
        dfs([], 0, 0)
        return res