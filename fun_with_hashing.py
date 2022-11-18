class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

def ascii(data):
    x = 0
    for i in data :
        x += ord(i)
    return x

def f(i):
    return i*i

class hash:
    # Code Here
    def __init__(self,maxSize,maxCollision):
        self.table = [None] *  maxSize
        self.size = 0
        self.maxSize = maxSize
        self.maxCollision = maxCollision
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size >= self.maxSize

    def add(self,data, i = 0):
        index = (ascii(data.key) + f(i))% self.maxSize #i คือจำนวนการชน
        if self.isEmpty():
            self.table[index] = data
            self.size += 1
        elif self.table[index] == None and i < self.maxCollision:
                self.table[index] = data
                self.size += 1
        elif self.table[index] != None and i < self.maxCollision:
            print("collision number {0} at {1}".format(i+1,index))
            self.add(data,i+1)
        elif i >= self.maxCollision :
            print("Max of collisionChain")
    
    def printTable(self):
        for i in range(self.maxSize) :
                print("#{0}	{1}".format(i+1,self.table[i]))

inp = input(" ***** Fun with hashing *****\nEnter Input : ").split("/")
tableSize , maxCollision = int(inp[0][0]) , int(inp[0][2])
data = inp[1].split(",")
h = hash(tableSize,maxCollision)
for i in data :
    item = i.split()
    key , value = item[0],item[1]
    h.add(Data(key,value))
    h.printTable()
    print("---------------------------")
    if h.isFull():
        print("This table is full !!!!!!")
        break
    

