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
    elif value >= self.right:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass