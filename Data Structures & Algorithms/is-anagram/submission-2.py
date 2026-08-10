class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t): # if not same length its false 
                return False

            countS, countT = {}, {}   ## create 2 hash maps
            
            for i in range(len(s)): ## we run through range of lenth of string 
                countS[s[i]] = 1 + countS.get(s[i], 0) ## we count how many times character i was in the string so we use the get function to see the count and add 1
                countT[t[i]] = 1 + countT.get(t[i], 0)
            for c in countS: ## we run the keys through the hashmap
                if countS[c] != countT.get(c, 0): ## if the key isnt the same value as they key in other hashmap its false
                    return False
            return True 


        
