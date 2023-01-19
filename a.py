class Queue:
    def __init__(self, size=None) -> None:
        self.size = size
        self.__l = []
        self.__l_size = 0

    def enqueue(self, ele) -> None:
        self.__l[-1] = ele
        self.__l_size += 1

    def dequeue(self) -> None:
        del self.__l[0]
        self.__l_size -= 1
    
<<<<<<< HEAD
<<<<<<< HEAD
print(isinstance(int, str))
print("new line"
        )
=======
#print(isinstance(int, str))
>>>>>>> parent of 9892b83 (added new print line)
=======
#print(isinstance(int, str))
>>>>>>> parent of 9892b83 (added new print line)
