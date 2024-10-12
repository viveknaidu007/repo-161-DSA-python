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
    
    def insert_after_value(self, data_after, data):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        elif data_after == self.head.data:
            node = Node(data, self.head.next)
            self.head.next = node
            return
        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    itr.next = Node(data, itr.next)
                    break
                itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        elif data == self.head.data:
            self.head = self.head.next
            return
        else:
            itr = self.head
            while itr:
                if data == itr.next.data:
                    itr.next = itr.next.next
                    break
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
    ll.insert_list(["banana","mango","grapes","orange"])
    # ll.print()
    ll.insert_after_value("banana","apple") # insert apple after banana
    # ll.print()
    ll.insert_after_value("mango","kiwi") # insert kiwi after mango
    # ll.print()
    ll.insert_after_value("orange","dragonfruit") # insert dragonfruit after orange
    ll.print()
    
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()