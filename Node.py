class Node:
  def __init__(self, name):
    self.name = name
    self.adjacents = {}

  def add_adjacent(self, node, distance, time):
    self.adjacents[node] = (distance, time)
