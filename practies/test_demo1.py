def addtwo():
    nums = [3,2,4]
    target = 6
    rnums = []
    i = 0
    for n in nums:
        i = i
        j = 0
        for m in nums:
            j = j
            firstItem = n
            secItem = m
            if firstItem + secItem == target and i != j:
                rnums.append(i)
                rnums.append(j)           
                return rnums
            j=j+1
        i=i+1
    
#result = addtwo()
#print(result)

def palindromenumber():
    x = -121
    strightnum = str(x)
    reversenum = str(x)[::-1]
    if strightnum == reversenum:
        return True
    else:
        return False
#result1 = palindromenumber()
#print(result1)
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strnum = str(s)
        count = 0
        resdic = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
        a = 0
        for n in strnum[::-1]:
            b = resdic.get(n) 
            a = int(a) + int(b)
        return a
'''
def roman(s):
    resdic = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    for i in range(len(s)):
        

        n = ""  
        i = i + r      
        if i >= (len(s)):
            break
        if s[i] == "C" and i + 1 < (len(s)):
            if s[i+1] == "M":
                n = "CM"
                r = r + 1
        elif s[i] == "X" and i + 1 < (len(s)):
            if s[i+1] == "C":
                n = "XC"
                r = r + 1  
        elif s[i] == "I" and i + 1 < (len(s)):
            if s[i+1] == "V":
                n = "IV"
                r = r + 1  
            elif s[i+1] == "X":
                    n = "IX"
                    r = r + 1
        if n == "":
            n = s[i]
        b = resdic.get(n) 
        a = int(a) + int(b) 
    return a
result = roman("IX")#MCMXCIV#LVIII
print(result)