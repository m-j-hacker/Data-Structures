class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # 
    # My initial thought is to make our storage into a list
    # 
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage) > 0:
      self.storage.pop(0)
      for i in range(1, len(self.storage)):
        self.storage[i-1] = self.storage[i]

  def len(self):
    return len(self.storage)
