class Solution:
    def printSequence(self,S):
        # code here
        arr = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999"]
        n = len(S)
        output = ""
        for char in S:
            if char is " ":
                output += "0"
            else:
                position = ord(char)-ord("A")
                output += arr[position]
        return output
