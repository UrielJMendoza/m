class Solution:
    def countBits(self, n: int) -> List[int]:
        ## convert  0 to n to binary then count the number of 1s in each number converted into binary and we will use sum for each binary number and then append it to a array then move on to the next number till done
        ArrayofBits = []


        for i in range(n+1):
            currentNum = i
            Total = 0
            while currentNum >= 1:
                if currentNum % 2 == 1:
                    Total +=1 

                currentNum = currentNum // 2
            ArrayofBits.append(Total)

        return ArrayofBits

        