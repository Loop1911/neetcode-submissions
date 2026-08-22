class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]
        #isallnum make the space in words poof and we do char.lower to implement lowercase 
        #then we do reverse the string
