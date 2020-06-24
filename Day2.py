class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        for i in range(0, len(nums)):
            for j in range (i+0 len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#################################################################

class MyQueue:

    def __init__(self, key, value):
        """
        Initialize your data structure here.
        """
        self.key = key
        self.value = value

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        def dequeue(self):
        self.size -= 1
         return self.storage.remove_from_head()

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()                    