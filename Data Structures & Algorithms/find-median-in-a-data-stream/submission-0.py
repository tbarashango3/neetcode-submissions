class MedianFinder:

    def __init__(self):
        #initialize median finder class
        # intialize with empty list 
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr = sorted(self.arr)
        # add number to list/array 
        # sort list
        # append number to end of list and then sort
        

    def findMedian(self) -> float:
        # return the median of current list 
        # if the length of the array is even, then we return the average
        # if length of the array is odd, then we return the middle value
        arr = self.arr
        n = len(arr)
        # len(arr) = 7, indexes are 0-6, and we would return index 4
        # to calculate middle element, we do (n - 1) // 2 + 1
        # if n == 6,we have indexes  0, 1, 2, 3, 4, 5
        #print(6 // 2)

        if n % 2 == 1:
            ans = float(arr[n // 2])
            return ans
        right = n // 2
        left = right - 1
        avg = float((arr[left] + arr[right]) / 2)
        return avg

class Test:
    if __name__ == "__main__":
        medianFinder = MedianFinder()
        print(medianFinder.addNum(1))
        print(medianFinder.findMedian())
        print(medianFinder.addNum(3))
        print(medianFinder.findMedian())
        print(medianFinder.addNum(2))
        print(medianFinder.findMedian())
        

        
        