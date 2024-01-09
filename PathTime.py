class Dijkstra:
  def __init__(self, graph):
      self.graph = graph

  def shortest_path(self, start_name, end_name):
      shortest_times = {node: float('infinity') for node in self.graph.nodes}
      shortest_times[start_name] = 0
      unvisited = set(self.graph.nodes.keys())

      while unvisited:
          current_node_name = min(unvisited, key=lambda node: shortest_times[node])
          current_node = self.graph.nodes[current_node_name]

          if shortest_times[current_node_name] == float('infinity') or current_node_name == end_name:
              break

          for adjacent, (edge_distance, edge_time) in current_node.adjacents.items():
              time = shortest_times[current_node_name] + edge_time

              if time < shortest_times[adjacent.name]:
                  shortest_times[adjacent.name] = time

          unvisited.remove(current_node_name)

      return shortest_times[end_name] if shortest_times[end_name] != float('infinity') else None
