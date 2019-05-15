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
    self.size += 1
  
  def dequeue(self):
    if len(self.storage) > 0:
      self.storage.pop(0)
      self.size -= 1
    else:
      return None

  def len(self):
    return self.size
