# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #print(l1)
        #print(l2)
        sumList1 = sumLinkedList(l1)
        sumList2 = sumLinkedList(l2)
        sumResult = sumList1 + sumList2
        result = intToLinkedList(sumResult)
        #print(f'The sum1 {sumList1} and sum2 {sumList2}. The sum of this is: {sumResult}')
        #print(f'The final result is:{result}')
        return result

def sumLinkedList(l: ListNode) -> int:
    c = result = 0   
    while l is not None:
        result = result + l.val*(10**c)
        l = l.next
        c+=1
    return result

def intToLinkedList(num: int) -> ListNode:
    numString =  str(num)
    last = len(numString)-1
    curr = head = ListNode(numString[last])
    for y in range (1,len(numString)):
        number = int(numString[last-y])
        curr.next = ListNode(number)
        curr = curr.next
    return head

solutionOne = Solution()

print(solutionOne.addTwoNumbers([2,4,3],[5,6,4]))