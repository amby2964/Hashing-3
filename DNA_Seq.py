class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        output = set([])
        substr = set([])
        for i in range(0,len(s)-9):
            sub_str = s[i:i+10]
            if(sub_str in substr):
                output.add(sub_str)
            else:
                substr.add(sub_str)
        return output
