
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
##check base base t is empty

        countT = {}
        window = {}
##create two hash maps of counts and widnow
##add all the chars in t into count
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have = 0##create a have variable and a need varaible
        need = len(countT)

        res = [-1,-1]##make res and have as low as posible 
        resLen = float("infinity")

        l = 0
##initalize left pointer then go through the string s 
        for r in range(len(s)):
            ## go through all values in s 
            c = s[r] # make c equal to the value of the index in s
            window[c] = 1 + window.get(c,0) ## then we add into the window the value of s [r] + = 

#if the value is in is in the hashmap count that ha the T values in and the window at c  === count[c] meaning we have a value in the window that is in t hashmap that we need 
            if c in countT and window[c] == countT[c]:
                have += 1 ## then we increment have
            while have == need: ##if the condition where we have all the values we need
                if (r - l +1) < resLen: ## then we check if its smaller than the past res len
                    res = [l,r] ## if it is then we make res equal to left and right
                    resLen = (r - l + 1) ## and update the smallest sub arryy

                window[s[l]] -= 1##then we decrement the left side to try and make it smaller
                if s[l] in countT and window[s[l]] < countT[s[l]]: ## if the string at the left inter is in count  and the window is smaller than the count then we chnage our have down
                    have -= 1
                l += 1 ## then we increment left

        l, r = res ## return our results of our work
        return s[l: r+1] if resLen != float("infinity") else ""


    

                
                
            

        
        
