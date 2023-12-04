class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return NONE
    def is_empty(self):
        return len(self.stack) == 0

def reverse_sentence(sentence):
    words = sentence.split()
    stack = Stack()
    for word in words:
        stack.push(word)
    reversed_sentence = ""
    while not stack.is_empty():
        reversed_sentence += stack.pop()+ ""
    return reversed_sentence.strip()
T = int(input())
test_cases = [input() for _ in range(T)]
for sentence in test_cases:
    reversed_sentence = reverse_sentence(sentence)
    print(reversed_sentence)
        