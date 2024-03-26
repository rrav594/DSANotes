def subsetSum(num: List[int]) -> List[int]:
    res = []
    def backtrack(i, total):
        if i == len(num):
            res.append(total)
            return
        backtrack(i+1, total+num[i])
        backtrack(i+1, total)

    backtrack(0, 0)
    res.sort()
    return res