class RequestLogger:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.message_map = {}

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        if len(self.message_map) == 0 or not request in self.message_map:
            self.message_map[request] = timestamp
            return True

        value = self.message_map[request]
        if (timestamp - value) >= self.time_limit:
            self.message_map[request] = timestamp
            return True
        else:
            return False
# driver code
def main():
    new_requests = RequestLogger(7)

    times = [1, 5, 6, 7, 15]
    messages = ["good morning",
                "hello world",
                "good morning",
                "good morning",
                "hello world"]

    for i in range(len(messages)):
        print(i + 1, ".\t Time, Message: {",
              times[i], ", '", messages[i], "'}", sep="")
        print("\t Message request decision: ",
              new_requests.message_request_decision(
                times[i], messages[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
