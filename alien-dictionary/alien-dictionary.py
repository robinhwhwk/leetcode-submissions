class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(list(set(words[0])))
        prereqs = collections.defaultdict(set) # maps prereqs: dependents
        prereq_count = collections.defaultdict(int) # maps dependents: prereqs left
        for i in range(len(words)-1):
            # for each word, look at all the words after it
            for j in range(i + 1, len(words)):
                # for each word after, match the letters until we get a mismatch
                p1 = p2 = 0
                s1, s2 = words[i], words[j]
                for c in s1:
                    if c not in prereq_count:
                        prereq_count[c] = 0
                for c in s2:
                    if c not in prereq_count:
                        prereq_count[c] = 0
                while p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
                    p1 += 1
                    p2 += 1
                if p1 < len(s1) and p2 == len(s2):
                    return ""
                if p1 < len(s1) and s2[p2] not in prereqs[s1[p1]]:
                    prereqs[s1[p1]].add(s2[p2])
                    prereq_count[s2[p2]] += 1
                    
        queue = [ch for ch, count in prereq_count.items() if count == 0]
        result = ""
        while queue:
            # process characters without dependencies
            current_char = queue.pop(0)
            result += current_char
            for dependent in prereqs[current_char]:
                prereq_count[dependent] -= 1
                if prereq_count[dependent] == 0:
                    queue.append(dependent)
    
        return result if max(prereq_count.values()) == 0 else ""
                



