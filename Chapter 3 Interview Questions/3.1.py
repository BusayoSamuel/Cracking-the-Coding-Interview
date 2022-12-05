"""
Three in One: Describe how you could use a single array to implement three stacks.
"""

#Fixed Approach
class Three_in_one():
    num_of_stacks = 3
    size = None
    array = None

    def __init__(self, size: int) -> None:
        self.array = [None] * self.num_of_stacks * size
        self.size = size


    def push(self, stackNum: int, item) -> None:
        index = stackNum * self.num_of_stacks
        step = 0
        while self.array[index] != None and step < self.size:
            index += 1
            step += 1

        if self.array[index] == None:
            self.array[index] = item
        else:
            print("Stack is full")

    def pop(self, stackNum: int):
        index = stackNum * self.num_of_stacks
        step = 0
        while self.array[index + 1] != None and step < self.size:
            index += 1
            step += 1

        item = self.array[index]
        self.array[index] = None

        return item

    def peek(self, stackNum: int):
        index = stackNum * self.num_of_stacks
        step = 0
        while self.array[index + 1] != None and step < self.size:
            index += 1
            step += 1

        item = self.array[index]

        return item

    def isEmpty(self, stackNum) -> bool:
        index = stackNum * self.num_of_stacks

        return self.array[index] == None


new_array = Three_in_one(3)
new_array.push(0, 5)
new_array.push(0, 10)
new_array.push(1, 11)
print(new_array.peek(0))
print(new_array.isEmpty(2))





