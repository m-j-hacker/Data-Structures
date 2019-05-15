"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value, None)

    # Case for empty linked list
    if not self.head:
      self.head = new_node
      self.tail = new_node
    elif not self.head.next:
      new_node.next = self.head
      self.head = new_node
    else:
      self.insert_before(value)

  def remove_from_head(self):
    # If the linked list is empty it will not have a head
    if not self.head:
      return None

    # This condition means that we only have 1 item in our list
    if not self.head.next:
      head = self.head
      self.head = None
      self.tail = None
      return head.value

    # This condition is for a list with more than 1 item
    else:
      value = self.head.value
      self.head = self.head.next
      return value

  def add_to_tail(self, value):
    new_node = ListNode(value)

    # This case is for empty lists
    if self.tail is None:
      self.head = new_node
      self.tail = new_node

    else:
      # We will set the current reference's next to the new reference and make that the tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    # If there is no tail, the list is empty
    if not self.tail:
      return None

    # This condition is for only 1 item in the list
    if not self.tail.prev:
      tail = self.tail
      self.head = None
      self.tail = None
      return tail.value
    
    else:
      tail = self.tail
      self.tail.prev.next = None
      self.tail = self.tail.prev
      return tail.value

  def move_to_front(self, node):
    # This function should move a given node to the front of the list, it will remove the node and add it to the head

    # If there is no head, the list is empty
    if not node:
      return None
    
    # If there is only one item, make no change
    elif self.head == self.tail:
      pass

    # Otherwise, move an item to the front
    else:
      self.head.prev = node
      node.next = self.head
      node.prev = None
      self.head = node
      

  def move_to_end(self, node):
    self.tail.next = node
    node.next = None
    node.prev = self.tail
    self.tail = node

  def delete(self, node):
    if not node:
      return None
    else:
      node.delete()
    
  def get_max(self):
    current = self.head
    current_max = 0
    while current.next:
      if self.value > current_max:
        current_max = self.value
    return current_max
