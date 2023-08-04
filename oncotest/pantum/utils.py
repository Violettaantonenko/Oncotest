

class DataMixin:
    def get_user_context(self,**kwargs):
        context=kwargs
        return context

class Queue:
    FIFO='FIFO'
    LIFO='LIFO'
    STRATEGIES = [FIFO, LIFO]

    def __init__(self,strategy):
        if strategy not in self.STRATEGIES:
            raise ValueError(f' {strategy} not in supported strategies: {self.STRATEGIES}')
        self.storage = []
        self.strategy = strategy
    def add(self,value):
        if self.strategy == self.FIFO:
            self.storage.insert(0,value)
        elif self.strategy == self.LIFO:
            self.storage.append(value)

    def pop(self):
        if self.storage:
            if self.strategy == self.FIFO:
                return self.storage.pop(0)
            elif self.strategy == self.LIFO:
                return self.storage.pop()
        return None
