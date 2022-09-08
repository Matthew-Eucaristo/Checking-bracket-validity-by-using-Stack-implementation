class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def push(self, data):
        if self.top:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = Node(data)

    def pop(self):
        if self.isEmpty():
            raise Exception

        data_popped = self.top.data
        self.top = self.top.next
        return data_popped

    def peek(self, index=0):
        # index teratas adalah 0
        if self.isEmpty():
            raise Exception
        
        temp_node_sementara = []
        for val in self:
            temp_node_sementara.append(val)
        
        return temp_node_sementara[index]

    def isEmpty(self) -> bool:
        for node in self:
            return False
        return True

    def __iter__(self):
        node_now = self.top
        while node_now:
            yield str(node_now)
            node_now = node_now.next