class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
    
    def insert_list(self, myList: list):
        self.head = None
        for data in myList:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_index(self, index):
        if index<0 or index > self.get_length():
            raise IndexError(f"{index} is an Invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                count += 1
                itr = itr.next
    
    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            raise IndexError(f"{index} is an Invalid index")
        elif index == 0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                count+=1
                itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            itr = self.head
            llstr = ''

            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_list(['charan', 'dheeraj', 'sushanth', 'tyson'])
    # ll.print()
    # print(ll.get_length())

    # ll.remove_index(2)
    # ll.print()
    # print(ll.get_length())

    # ll.insert_at(1, 'abhi')
    # ll.print()
    # print(ll.get_length())

    ll.insert_list([10, 20, 30, 40, 50])
    ll.print()
    print(ll.get_length())

    ll.remove_index(2)
    ll.print()
    print(ll.get_length())

    ll.insert_at(1, 15)
    ll.print()
    print(ll.get_length())