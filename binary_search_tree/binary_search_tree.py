class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # first, we need to determine if the value is less or greater than self.value

    # If value is less than and there is not already a value on the left, assign value to left
    if value < self.value:

      if not self.left:
        self.left = BinarySearchTree(value)
    # If there is a value on the left already, run insert recursively
      else:
        self.left.insert(value)

    # If value is greater than or equal to self.value, assign value to right
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # Here we need to determine if the target can be found in the search tree
    if target.value == self.value:
      return self.value
    if target.value < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)


  def get_max(self):
    current_max = self.value
    current = self
    while current:
      if current_max < current.value:
        current_max = current.value
      current = current.right
      

  def for_each(self, cb):
    # This function will use the callback on each item in the tree
    # while self.right or self.left:
    #   cb(self)
    #   if self.right and self.left
    pass
