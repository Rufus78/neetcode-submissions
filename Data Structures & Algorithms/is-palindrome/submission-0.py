class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""

        for ch in s:
            if ch.isalnum():
                k += ch.lower()

        if k == k[::-1]:
            return True
        else:
            return False

        