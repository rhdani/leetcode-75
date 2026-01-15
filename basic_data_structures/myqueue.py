from Stack import Stack

class MyQueue(object):

    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()
        
    def push(self, x):
        self.enqueue.push(x)
            
    def pop(self):
        if self.dequeue.is_empty():
            for i in range(self.enqueue.size()):
                self.dequeue.push(self.enqueue.pop())
        return self.dequeue.pop()
        
    def peek(self):
        if self.dequeue.is_empty():
            for i in range(self.enqueue.size()):
                self.dequeue.push(self.enqueue.pop())
        return self.dequeue.top()

    def empty(self):
        return self.enqueue.is_empty() and self.dequeue.is_empty()

# Driver code
def main():
    input_queues = [
        [[9, 3, 1, "", "", ""], ["push", "push", "push", "pop", "peek", "empty"]],
        [[10, 6, "", "", ""], ["push", "push", "pop", "empty", "peek"]],
        [[1, 2, 3, "", "", "", "", ""], ["push", "push", "push", "peek", "pop", "pop", "pop", "empty"]],
        [[14, "", 66, ""], ["push", "pop", "push", "pop"]],
        [[4, ""], ["push", "peek"]]]
    for i in range(len(input_queues)):

        print(i + 1, ".\t Starting operations:", sep="")

        # initialize a queue
        queue_obj = MyQueue()
        # loop over all the commands
        for j in range(len(input_queues[i][1])):
            if input_queues[i][1][j] == "push":
                inputstr = input_queues[i][1][j] + \
                    "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, sep="")
                queue_obj.push(input_queues[i][0][j])
            if input_queues[i][1][j] == "pop":
                inputstr = input_queues[i][1][j] + \
                    "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, "   returns ",
                      queue_obj.pop(), sep="")
            if input_queues[i][1][j] == "empty":
                inputstr = input_queues[i][1][j] + \
                    "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, " returns ",
                      queue_obj.empty(), sep="")
            if input_queues[i][1][j] == "peek":
                inputstr = input_queues[i][1][j] + \
                    "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, "  returns ",
                      queue_obj.peek(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()
