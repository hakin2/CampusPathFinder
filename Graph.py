from Node import Node

class Graph:
  def __init__(self):
      self.nodes = {}

  def add_node(self, name):
      node = Node(name)
      self.nodes[name] = node
      return node

  def add_edge(self, node1, node2, distance, time):
      if node1 not in self.nodes:
          self.add_node(node1)
      if node2 not in self.nodes:
          self.add_node(node2)

      self.nodes[node1].add_adjacent(self.nodes[node2], distance, time)
      self.nodes[node2].add_adjacent(self.nodes[node1], distance, time)

  def display(self):
    for node in self.nodes.values():
      print(node.name, ":", ", ".join([f"{adj.name}({dist} ft, {time} min)" for adj, (dist, time) in node.adjacents.items()]))

