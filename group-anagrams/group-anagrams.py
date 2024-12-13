class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            count = [0 for _ in range(26)]
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            hash_tuple = tuple(count)
            if hash_tuple not in hashmap:
                hashmap[hash_tuple] = []
            hashmap[hash_tuple].append(s)
        return list(hashmap.values())