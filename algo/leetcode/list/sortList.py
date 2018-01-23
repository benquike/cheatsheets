# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        ret = '[' + str(self.val) + ','
        t = self.next
        while t != None:
            ret = ret + str(t.val) + ','
            t = t.next
        ret = ret + ']'

    def __repr__(self):
        return self.__str__()
    
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        t1 = head
        t1_prev = head
        t2 = head
        
        while t2 != None:
            t2 = t2.next
            
            if t2 == None:
                break
            
            t2 = t2.next
            t1_prev = t1
            t1 = t1.next
        
        t1_prev.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(t1)
        print 'h1 = ' + str(h1)
        print 'h2 = ' + str(h2)
        ret = None
        ret_t = None
        while True:
            if h1 == None:
                if ret == None:
                    return h2
                else:
                    ret_t.next = h2
                    return ret
            elif h2 == None:
                if ret == None:
                    return h1
                else:
                    ret_t.next = h1
                    return ret
            else:
                smaller = h1
                if smaller.val > h2.val:
                    smaller = h2
                    h2 = h2.next
                else:
                    h1 = h1.next

                if ret == None:
                    ret = smaller
                    ret_t = smaller
                else:
                    ret_t.next = smaller
                smaller.next = None
            
        return ret

def createList(l):
    ret = None
    t = None
    for i in l:
        if t == None:
            x = ListNode(i)
            ret = x
            t = x
        else:
            t.next = ListNode(i)
    return ret

if __name__ == '__main__':
    s = Solution()
    lst = createList([3,2,4])
    print str(lst)
    print s.sortList(createList([3,2,4]))
