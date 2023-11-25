class Anagram():
    # leetcode 242 = return true if input string t is an anagram of s and false otherwise
    def SortedSolution(s, t):
        return sorted(s) == sorted(t)