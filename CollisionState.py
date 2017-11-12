class CollisionState:
  def __init__(self, left = False, right = False, below = False, above = False):
    self.Left = left
    self.Right = right
    self.Below = below
    self.Above = above