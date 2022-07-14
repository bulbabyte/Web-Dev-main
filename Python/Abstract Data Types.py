# Python List
myList = []
print(myList)

# Additoin of Elements in the List
myList.append(55)
myList.append(88)
myList.append(66)
print(myList)

# Removing elements from List using Remove() method
myList.remove(88)
print(myList)

# Removing element using the pop() method
myList.pop()
print(myList)

print("Manipulate List without append/remove/prop:")
myList = myList + [7,8]
print(myList)
print(myList[2])
del myList[2]
print(myList)

# Python Stack
class stacksArray:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self.data.pop()

myStack = stacksArray()
myStack.push("Tokyo")
myStack.push("Osaka")
myStack.push("Nara")
print(myStack.data)
print(myStack.pop())
print(myStack.data)

# Python Queue
class queuesArray:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self.data.pop(0)


myQueue = queuesArray()
myQueue.push("Mel")
myQueue.push("Nina")
myQueue.push("Ruth")
print(myQueue.data)
print(len(myQueue))
print(myQueue.pop())
print(myQueue.data)
