class Solution(object):
    def partition(self, s):
        result=[]
        str1=[]

        def check(string_):
            return string_ == string_[::-1]
        
        def backtrack(start):
            if start == len(s):
                result.append(str1[:])
                return
        
            for end in range(start,len(s)):
                substr = s[start:end+1]
                if check(substr):
                    str1.append(substr)
                    backtrack(end+1)
                    str1.pop()
            
        backtrack(0)
        return result
