class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    self.storage.pop(0)
    self._bubble_up(len(self.storage) - 1)

  def get_max(self):
    pass

  def get_size(self):
    return len(self.storage - 1)

  # Helper function provided during lecture
  def _get_parent(self, index):
    return (index - 1) // 2
  
  def _bubble_up(self, index):
    # Index = index of item to bubble up
    while index > 0:
      # Find parent node first
      parent = self._get_parent(index)

      # We need to check to ensure that the parent node is larger
      # than the child node
      if self.storage[parent] < self.storage[index]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        index = parent
      else:
        break

  def _sift_down(self, index):
    heap_size = self.get_size()
    left_child_index = index * 2 + 1

    while self.storage


