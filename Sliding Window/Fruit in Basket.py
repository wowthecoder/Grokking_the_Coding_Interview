class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 1
        start, end = 0, 0
        typeFreq = {}
        while (end < len(fruits)):
            typ = fruits[end]
            n = len(typeFreq)
            if (n <= 1 or (n == 2 and typ in typeFreq)):
                typeFreq[typ] = typeFreq.get(typ, 0) + 1 
                end += 1
            else:
                sTyp = fruits[start]
                typeFreq[sTyp] -= 1
                if (typeFreq[sTyp] == 0):
                    typeFreq.pop(sTyp)
                maxLen = max(maxLen, end - start)
                start += 1
        maxLen = max(maxLen, end - start)
        return maxLen