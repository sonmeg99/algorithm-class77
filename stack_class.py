# define Stack class with push, pop, peek, is_empty, and size methods
class ArrayStack:
    def __init__(self, capacity):
        self.capcity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capcity - 1
    

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            print(f"PUSH: {item!r} -> stack is now {self.array[:self.top + 1]}")
        else:
            raise OverflowError("Stack Overflow")
        
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -=1
            print(f"POP : {item!r} -> stack is now {self.array[self.top + 1]}")
            return item
        else:
            raise IndexError("Stack underflow")
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
    # Test the Stack class
    def reverse_string(statement):
        print("\n[1] PUSH 단계 -----------------------")
        stack = ArrayStack(len(statement))
        for char in statement:
            stack.push(char)

        print("\n [2] POP단계 -----------------------")
        out = []
        while not stack.is_empty():
            out.append(stack.pop())

        result = ''.join(out)
        print("\n[3] 최종 결과 : {result}")
        return result

if __name__=="__main__":
    statement = "안녕하세요, 반갑습니다"
    reverse_string(statement)  