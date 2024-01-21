class StaticArray():
    def __init__(self,size):
        self.array=[None]*size
        self.size=size

    def __check_index__(self,i):
        if not (i>=0 and i<=(self.size-1)):
            raise IndexError('StaticArray index out of range')

    def get_at(self,i):
        self.__check_index__(i)
        return self.array[i]
        
    def set_at(self,i,x):
        self.__check_index__(i)
        self.array[i]=x

class ArraySequence(StaticArray):

    def __init__(self): #O(1)
        super().__init__(0)

    def __move_items__(self, from_index, to_index,step): #0(n)
        
        if step==1:
            start = to_index
            end = from_index-1
        else:
            start = from_index
            end = to_index+1

        for copy_index in range(start, end, -step):
            paste_index = copy_index + step
            self.set_at(paste_index, self.get_at(copy_index))
        
    def build(self,X): #O(n)
        super().__init__(len(X)) 
        for i,x in enumerate(X): 
            self.set_at(i,x) 

    def insert_at(self,i,x): #O(n)
        array_copy=self.array.copy()
        array_copy.append(None)
        self.build(array_copy)
        self.__move_items__(i,self.size-2,1)
        self.set_at(i,x)

    def delete_at(self,i): #O(n)
        del_val=self.get_at(i)
        self.__move_items__(i+1,self.size-1,-1)
        array_copy=self.array.copy()[:-1]
        self.build(array_copy)
        return del_val
        
    def insert_first(self,x): self.insert_at(0,x) #O(n)
    def delete_first(self): return self.delete_at(0) #O(n)
    def insert_last(self,x): self.insert_at(self.size-1,x) #O(n)
    def delete_last(self): return self.delete_at(self.size-1) #O(n)
