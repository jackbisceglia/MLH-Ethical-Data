class History:
    def __init__(self):
        self.queue = []

    def get_most_recent(self):
        return self.queue[0]

    def get_recents(self):
        return self.queue

    def update(self, command):
        if len(self.queue) >= 3:
            self.queue.pop(0)
        self.queue.append(command)