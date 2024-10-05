class Queue(): # main code start ---------------------------------------------------------------0
    def __init__(self):
        self.queue = []

    def enqueue(self, a): # adding to queue
        self.queue.append(a) # append a into the queue
    
    def dequeue(self, a): # removing from queue
        if len(self.queue) <= 0: # if queue is empty
            return None # return nothing
        return self.queue.pop(0) # if not then remove the first integer (0) [First in First out]
    
    def display(self): #print queue
        print(self.queue) 

    def dislen(self): #prints length of queue
        print(len(self.queue)) 
    
# main code end --------------------------------------------------------------------------------0

q = Queue() # object ---------------------------------------------------------------------------0

q.enqueue(1) # line 5
q.enqueue(2) # line 5   
q.enqueue(3) # line 5
q.enqueue(4) # line 5   
q.enqueue(5) # line 5

print('before removing:', q.display()) # line 13

q.dequeue(1) # line 8 
print('after removing:', q.display()) # line 13
