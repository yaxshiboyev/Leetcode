class Solution:
    def romanToInt(self, s: str) -> int:

    lookup = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    num = 0

    for i in range(len(s)):
        if i + 1 < len(s) and lookup[s[i]] < lookup[s[i+1]]:
            num -= lookup[s[i]]
        else:
            num += lookup[s[i]]
        return num


roman= input("enter roman number:")
ineger= Solution()


print(ineger.romanToInt(roman))
