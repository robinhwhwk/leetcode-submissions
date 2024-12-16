class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        total = 0
        i = 0
        while i < len(s):
            roman = s[i]
            if roman in "IXC" and i != len(s) - 1:
                if s[i:i+2] in romanDict:
                    total += romanDict[s[i:i+2]]
                    i += 1
                else:
                    total += romanDict[roman]
            else:
                # process normally
                total += romanDict[roman]
            i += 1
        return total
