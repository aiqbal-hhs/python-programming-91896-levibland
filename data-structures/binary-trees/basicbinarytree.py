# TODO: complete this

from typing import Optional

class Node:
  # A node has a data variable and two pointers, one for the left child node, and one for the right child node
  def __init__(self, data:int):
    self.data = data
    self.left = Optional[Node]
    self.right = Optional[Node]
