import queue
q1 = queue.Queue()
q1.put(10)
print(q1.get())
for i in range(20):
    q1.put(i)
while not q1.empty():
    print("the value",q1.get())