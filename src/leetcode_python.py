import time

class LeetCode49():
    def BruteForceSolution(strs):
        dictionary = dict()
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in dictionary:
                dictionary[sortedString].append(string)
            else:
                dictionary.update({sortedString : [string]})
        anagrams = []
        for key in dictionary:
            anagrams.append(dictionary[key])
        return anagrams

class LeetCode66():
    def BruteForceSolution(nums):
        i = len(nums)-1
        while i >= 0:
            nums[i] += 1
            if nums[i] == 10:
                nums[i] = 0
                i -= 1
            else:
                i = -1
        if nums[0] == 0:
            nums.append(1)
            nums.reverse()
        return nums
    def WrongBruteForceSolution(nums):
        lastDigit = nums[len(nums)-1]
        lastDigit += 1
        if lastDigit == 10:
            if (len(nums)-1 < 1):
                newArray = [1,0]
                return newArray
            else:
                nums[len(nums)-1] += 1
                return nums
        else:
            nums[len(nums)-1] = lastDigit
            return nums

class LeetCode217():
    # return true if any value appears at least twice in the array
    # return false if every element is distinct
    def BruteForceSolution():
        return True
    def OptimizedSolution(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False

class LeetCode242():
    # return true if input string t is an anagram of s and false otherwise
    def SortedSolution(s, t):
        return sorted(s) == sorted(t)

class LeetCode:
    # generate input
    def GetString(number):
        if number == 0:
            return " "
        elif number == 1:
            return "anagram"
        elif number == 2:
            return "nagaram"
        elif number == 3:
            return "test"
        else:
            return ""
    def GetArrayNumbers(number):
        if number == 0:
            return [" "]
        elif number == 1:
            return [1,2,3,4]
        elif number == 2:
            return [1,2,3,1]
        elif number == 3:
            return [9]
        elif number == 4:
            return [8,9,9]
        else:
            return []
    def GetArrayStrings(number):
        if number == 0:
            return [" "]
        elif number == 1:
            return ["eat","tea","tan","ate","nat","bat"]
        else:
            return []
    # leetcode problem testing
    def Test(number):
        if number == 49:
            TestStringArray1 = LeetCode.GetArrayStrings(1)
            print ("for " + str(TestStringArray1))
            startTime = time.time()
            print("sorted result: " + str(LeetCode49.BruteForceSolution(TestStringArray1)))
            print("%s seconds" % (time.time() - startTime))
        elif number == 66:
            TestArray1 = LeetCode.GetArrayNumbers(1)
            TestArray2 = LeetCode.GetArrayNumbers(2)
            TestArray3 = LeetCode.GetArrayNumbers(3)
            TestArray4 = LeetCode.GetArrayNumbers(4)
            print ("for " + str(TestArray1))
            startTime = time.time()
            print("brute: " + str(LeetCode66.BruteForceSolution(TestArray1)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + str(TestArray2))
            startTime = time.time()
            print("brute: " + str(LeetCode66.BruteForceSolution(TestArray2)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + str(TestArray3))
            startTime = time.time()
            print("brute: " + str(LeetCode66.BruteForceSolution(TestArray3)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + str(TestArray4))
            startTime = time.time()
            print("brute: " + str(LeetCode66.BruteForceSolution(TestArray4)))
            print("%s seconds" % (time.time() - startTime))
        elif number == 217:
            TestArray1 = LeetCode.GetArrayNumbers(0)
            TestArray2 = LeetCode.GetArrayNumbers(1)
            TestArray3 = LeetCode.GetArrayNumbers(2)
            print ("for " + str(TestArray1))
            startTime = time.time()
            print("optimized result: " + str(LeetCode217.OptimizedSolution(TestArray1)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + str(TestArray2))
            startTime = time.time()
            print("optimized result: " + str(LeetCode217.OptimizedSolution(TestArray2)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + str(TestArray3))
            startTime = time.time()
            print("optimized result: " + str(LeetCode217.OptimizedSolution(TestArray3)))
            print("%s seconds" % (time.time() - startTime))
        elif number ==242:
            TestString1 = LeetCode.GetString(1)
            TestString2 = LeetCode.GetString(2)
            TestString3 = LeetCode.GetString(3)
            print ("for " + TestString1 + "&" + TestString2)
            startTime = time.time()
            print("sorted result: " + str(LeetCode242.SortedSolution(TestString1, TestString2)))
            print("%s seconds" % (time.time() - startTime))
            print ("for " + TestString2 + "&" + TestString3)
            startTime = time.time()
            print("sorted result: " + str(LeetCode242.SortedSolution(TestString2, TestString3)))
            print("%s seconds" % (time.time() - startTime))
        else:
            print("ERROR: Incorrect number input")


# LeetCode.Test(217)
# LeetCode.Test(66)
LeetCode.Test(49)