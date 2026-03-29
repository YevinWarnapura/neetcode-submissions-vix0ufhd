class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        currCounter = 0
        comprCounter = 0
        for currNum in nums:
            for comprNum in nums:
                if currNum == comprNum and comprCounter != currCounter:
                    return True  
                comprCounter += 1
            comprCounter = 0
            currCounter += 1   
        return False
            