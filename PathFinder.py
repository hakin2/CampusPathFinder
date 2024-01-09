from PathTime import Dijkstra

class SchedulePathFinder:
  def __init__(self, graph, dijkstra):
      self.graph = graph
      self.dijkstra = dijkstra

  def find_shortest_path_for_schedule(self, schedule):
      total_time = 0
      path = []

      for i in range(len(schedule) - 1):
          start_building = schedule[i]
          end_building = schedule[i + 1]
          time = self.dijkstra.shortest_path(start_building, end_building)
          if time is None:
              print(f"No path found between {start_building} and {end_building}.")
              return None
          total_time += time
          path.append((start_building, end_building, time))

      return path, total_time
