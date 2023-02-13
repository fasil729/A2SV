class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str=""
        ctr = 0
        longest_counter=0
        
        for i in s:
            
            if i not in sub_str  :
                
                ctr +=1
                sub_str+=i
                if longest_counter<ctr:
                    longest_counter=ctr
            else :
                j=sub_str.find(i)+1
                sub_str=sub_str[j:]
                sub_str+=i
                ctr=len (sub_str)
                
                if longest_counter<ctr:
                    longest_counter=ctr
        return longest_counter