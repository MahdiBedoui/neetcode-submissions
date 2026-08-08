class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            countS, countT = {}, {}   ## create 2 hash maps

            if len(s) != len(t): # if not same length its false 
                return False

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True 


        
