class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            hash_string = "".join(sorted(s))
            if hash_string not in hashmap:
                hashmap[hash_string] = []
            hashmap[hash_string].append(s)
        return list(hashmap.values())