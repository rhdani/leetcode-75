print("\n\tInitializing the queues")
        # Declaring an array of two queues
        queues = [deque(), deque()]
        print("\t\tqueues array: ", queues, sep = "")
        # Initializing the current and next queues
        current_queue = queues[0]
        next_queue = queues[1]
        print("\t\tCurrent queue: ", current_queue)
        print("\t\tNext queue: ", next_queue)

        # Enqueuing the root node into the current queue and setting
        # level to zero
        print("\t\tEnqueuing the root node into the current queue")
        current_queue.append(root)
        print("\t\t\tUpdated current queue: ", printing_queue(current_queue))
        level_number = 0
        print("\t\t\tLevel number: ", level_number)

        print("\n\tIterating the current queue")
        n = 0
        while current_queue:
            print("\t\tLoop iteration ", n, sep = "")
            n += 1

