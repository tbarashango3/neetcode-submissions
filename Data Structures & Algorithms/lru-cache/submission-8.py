class LRUCache:

    def __init__(self, capacity: int):
        #LRU must have size capacity
        self.m = {}
        self.capacity = capacity
        self.s = []
        self.size = 0
        

    def get(self, key: int) -> int:
        m = self.m
        numset = self.s
        if key in m:
            numset.remove(key)
            numset.append(key)
            return m[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        numset = self.s
        m = self.m
        if key in numset:
            numset.remove(key)
        else:
            self.size += 1
        numset.append(key)
        #numset = (1, 2, 3)
        m[key] = value
            #m[1] = 10
            #m[2] = 20
            #m[3] = 30
        #if len(s) > capacity, then we remove s[0]
        #len(numset) == 3, size == 2
        if self.size > self.capacity:
            #m[1] = -1
            #numset = (2, 3)
            del m[numset[0]]
            del numset[0]
            
            self.size -= 1
        #print(numset)
        #print("map: ",self.m)
        #print("list: ", self.s)
        
            
        

        

        
