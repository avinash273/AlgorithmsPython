pointer = 0
class Solution:
    def strStr(haystack: str, needle: str) -> int:
        hay_size = len(haystack)
        needle_size = len(needle)
        if(needle_size == 0):
            return 0
        else:
            for i in range(hay_size):
                j = 1
                if(needle[0] == haystack[i]):
                    pointer = i
                    if(needle == haystack[i:i+needle_size]):
                        return pointer
        return -1

haystack = "hello"
needle = "ll"

print(Solution.strStr(haystack, needle))