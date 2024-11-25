class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            hash_string = ''.join(sorted(string))
            if hash_string not in anagrams:
                anagrams[hash_string] = []
            anagrams[hash_string].append(string)
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res

