class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleaned += s[i].lower()

        backwards = ""

        i = len(cleaned) - 1
        while i >= 0:
            backwards += cleaned[i]
            i -= 1
        
        if cleaned == backwards:
            return True
        return False
