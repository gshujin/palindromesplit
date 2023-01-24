def chop(s):

    list=[]

    def isPalindrome(s):
        """determines if s is a palindrome"""
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        return False

    def finds_number_of_palindrome(s,list):
        sum = 0
        for i in range(len(s)):
            for x in range(i+2,len(s)+1):
                temp1 = s[i:x]
                if isPalindrome(temp1):
                    sum = sum+1
                    
                    temp2 = s[x:]
                    finds_number_of_palindrome(temp2,list)                    
        
        list.append(int(sum))
        return list

    x = finds_number_of_palindrome(s,list)
    total = 1 + sum(x)
    return total

