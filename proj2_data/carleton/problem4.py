import sys
class Min_Heap:
    def __init__(self):
        self.a = []
    def insert(self, x):
        i = self.size()
        self.a.append(x)
        self.min_heapify_bottomup(i)
    def remove(self):
        to_return = self.look()
        if to_return != "HeapError":
            last = self.a.pop()
            if to_return != last:
                self.a[0] = last
                self.min_heapify(0)
        return to_return
         
    def look(self):
        if not self.is_empty():
            return self.a[0] 
        else:
            return "HeapError"
    def size(self):
        return len(self.a)
    def is_empty(self):
        if self.size() == 0:
            return True
        return False
    def to_string(self):
        if self.is_empty():
            return "Empty"
        s = ""
        size = self.size()
        for i in range(size):
            s+= str(self.a[i]) 
            if i != size-1:
                s+=" "
             
        return s
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l <=  self.size()-1 and self.a[l] < self.a[i]:
           smallest = l
        if r <= self.size()-1 and self.a[r] < self.a[smallest]:
            smallest = r
        if smallest != i:
            temp = self.a[i]
            self.a[i] = self.a[smallest]
            self.a[smallest] = temp
            self.min_heapify(smallest)
    def min_heapify_bottomup(self, i):
        p = self.par(i)
        if self.a[i] < self.a[p]:
            temp = self.a[i]
            self.a[i] = self.a[p]
            self.a[p] = temp
            self.min_heapify_bottomup(p)
    def left(self, i):
        return (2*i + 1)
    def right(self, i):
        return (2*i + 2)
    def par(self, i):
        return  0 if i == 0 else ((i-1)//2)


# self function runs the program according to the problem specification
def driver():
    h = Min_Heap();
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                h.insert(value)
            elif action == "remove":
                print(h.remove())
            elif action == "print":
                print(h.to_string())
            elif action == "size":
                print(h.size()) 
            elif action == "best": 
                print(h.look())

if __name__ == "__main__":
    driver()
